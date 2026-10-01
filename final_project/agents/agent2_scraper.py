from groq import Groq
from tools.scraper_tool import scrape_website
from database.db import get_unprocessed_leads, update_lead
from database.models import AgentState, Qualifier
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_scraper(state: AgentState) -> AgentState:
    print("⏳ Agent 2 running...")

    leads = get_unprocessed_leads()
    qualified = []

    for lead in leads:
        print(f"   Scraping: {lead['url']}")
        scraped = scrape_website(lead["url"])

        if "error" in scraped:
            update_lead(lead["id"], is_qualified=False, reason="scraping failed")
            continue

        # LLM decides using structured output
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{
                "role": "user",
                "content": f"""
                Analyze this company website and decide if they need a chatbot.
                
                Homepage: {scraped['homepage_text']}
                Contact page: {scraped['contact_text']}
                Emails found: {scraped['emails']}
                
                Rules:
                - If they already have a chatbot → is_qualified: false
                - If they don't need a chatbot → is_qualified: false  
                - If they need a chatbot but no email found → is_qualified: false
                - If they need a chatbot AND email found → is_qualified: true
                - For best_email: pick sales@, info@, hello@, contact@ over pr@, jobs@
                
                You MUST respond ONLY with this exact JSON format, no extra text:
                {{
                    "is_qualified": true,
                    "extracted_email": "email@example.com or null",
                    "reason": "short reason here"
                }}
                """
            }]
        )

        text = response.choices[0].message.content
        text = text.strip().replace("```json", "").replace("```", "").strip()

        if not text:
            update_lead(lead["id"], is_qualified=False, reason="LLM returned empty response")
            continue

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            update_lead(lead["id"], is_qualified=False, reason="LLM response not valid JSON")
            continue

        result = Qualifier(
            is_qualified=data.get("is_qualified", False),
            extracted_email=data.get("extracted_email") or data.get("email"),
            reason=data.get("reason") or data.get("explanation", "")
        )

        update_lead(
            lead["id"],
            is_qualified=result.is_qualified,
            email=result.extracted_email,
            reason=result.reason
        )

        if result.is_qualified:
            qualified.append(lead)

    state["qualified_leads"] = qualified
    print(f"✅ Agent 2 done — {len(qualified)} qualified")
    return state