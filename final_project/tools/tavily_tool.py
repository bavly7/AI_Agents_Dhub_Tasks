from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_companies(query: str) -> list:
    response = client.search(query, max_results=10)
    results = []
    for r in response["results"]:
        results.append({
            "company_name": r["title"],
            "url": r["url"]
        })
    return results