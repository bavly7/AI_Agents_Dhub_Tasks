"""
Test email generation using Groq — simulates what Agent 3 writes to real leads
"""

import os
import json
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

# Force load correct .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── Simulated leads from your database ──────────────────────────────────────
FAKE_LEADS = [
    {
        "company_name": "Cairo Bites Restaurant",
        "url": "https://cairobites.com",
        "email": "info@cairobites.com",
    },
    {
        "company_name": "Nile View Cafe",
        "url": "https://nileviewcafe.com",
        "email": "contact@nileviewcafe.com",
    },
    {
        "company_name": "Koshary El Tahrir",
        "url": "https://kosharyeltahrir.com",
        "email": "hello@kosharyeltahrir.com",
    },
    {
        "company_name": "Zamalek Grill House",
        "url": "https://zamalekgrill.com",
        "email": "reservations@zamalekgrill.com",
    },
]


def generate_email(lead: dict) -> dict:
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

    text = response.choices[0].message.content.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)


def run():
    print("\n🤖 Email Generation Simulation — Agent 3")
    print("=" * 60)
    print(f"  Simulating {len(FAKE_LEADS)} leads from database\n")

    for i, lead in enumerate(FAKE_LEADS, 1):
        print(f"{'='*60}")
        print(f"LEAD {i} — {lead['company_name']}")
        print(f"  📧 To:  {lead['email']}")
        print(f"  🌐 URL: {lead['url']}")
        print(f"{'='*60}")

        try:
            email = generate_email(lead)

            print(f"\n  📌 SUBJECT:\n  {email['subject']}")
            print(f"\n  📝 BODY:\n")
            for line in email["body"].split("\\n"):
                print(f"  {line}")
            print(f"\n  ✅ Generated successfully\n")

        except Exception as e:
            print(f"\n  ❌ Failed: {e}\n")

    print("=" * 60)
    print("✅ Simulation complete")
    print("=" * 60)


if __name__ == "__main__":
    run()