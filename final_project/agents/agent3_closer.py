from groq import Groq
from tools.email_tool import send_email
from database.db import get_qualified_leads, mark_email_sent
from database.models import AgentState, Closer
import os
from dotenv import load_dotenv
from pathlib import Path
import json

# Force load .env from project root
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_closer(state: AgentState) -> AgentState:
    print("⏳ Agent 3 running...")

    leads = get_qualified_leads()

    if not leads:
        print("❌ No qualified leads to email.")
        state["emails_sent"] = 0
        return state

    sent = 0
    for lead in leads:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{
    "role": "user",
    "content": f"""
    Write a short persuasive cold sales email offering AI chatbot services to {lead['company_name']}.
    
    Rules:
    - Sign as "The LeadFlow AI Team" (NOT Alex, NOT a single person)
    - Company name: "LeadFlow AI"
    - Under 150 words
    - Open with a strong hook about their business specifically
    - Highlight 2-3 clear benefits: 24/7 customer support, more bookings, instant FAQ answers
    - End with a strong CTA: "Let's connect — reply to this email or book a free 15-min demo at [your link]"
    - Tone: confident, human, exciting — NOT robotic or generic
    - Do NOT use placeholders like [Your Name] or [link]
    - Make it feel like a real opportunity they'd regret missing
    
    You MUST respond ONLY with this exact JSON format, no extra text:
    {{
        "subject": "email subject here",
        "body": "email body here"
    }}
    """
}]
        )

        text = response.choices[0].message.content
        text = text.strip().replace("```json", "").replace("```", "").strip()

        if not text:
            print(f"   ⚠️ Skipping {lead['company_name']} — LLM returned empty")
            continue

        try:
            data = json.loads(text)
            email_content = Closer(
                subject=data.get("subject", ""),
                body=data.get("body", "")
            )
        except json.JSONDecodeError:
            print(f"   ⚠️ Skipping {lead['company_name']} — invalid JSON")
            continue

        success = send_email(
            to_email=lead["email"],
            subject=email_content.subject,
            body=email_content.body
        )

        if success:
            mark_email_sent(lead["id"])
            sent += 1
            print(f"   ✅ Email sent to {lead['company_name']}")
        else:
            print(f"   ❌ Failed to send to {lead['company_name']}")

    state["emails_sent"] = sent
    print(f"✅ Agent 3 done — {sent} emails sent")
    return state