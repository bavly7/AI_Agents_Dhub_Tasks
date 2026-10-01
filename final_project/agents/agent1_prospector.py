from groq import Groq
from tools.tavily_tool import search_companies
from database.db import save_lead
from database.models import AgentState
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_prospector(state: AgentState) -> AgentState:
    print("⏳ Agent 1 running...")

    # LLM crafts the perfect search query
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{
            "role": "user",
            "content": f"""
            Create a specific Google search query to find real companies 
            that might need a chatbot based on this input: '{state["search_query"]}'
            
            Return ONLY the search query. Nothing else.
            Example: 'law firms in cairo egypt contact'
            """
        }],
        temperature=0.4
    )

    refined_query = response.choices[0].message.content.strip()
    print(f"🔍 Searching for: {refined_query}")

    companies = search_companies(refined_query)

    for company in companies:
        save_lead(company)

    state["leads"] = companies
    print(f"✅ Agent 1 done — found {len(companies)} companies")
    return state