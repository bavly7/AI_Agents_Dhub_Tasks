"""
Full diagnostic test for Agent 3 (Closer)
Tests: env config, LLM generation, email connection, and full send
"""

import os
import sys
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path

# Force load .env from project root (one level up from tests/)
env_path = Path(__file__).resolve().parent.parent / ".env"
print(f"\n📄 Loading .env from: {env_path}")
load_dotenv(dotenv_path=env_path, override=True)

# ─────────────────────────────────────────────
# STEP 1 — Check .env configuration
# ─────────────────────────────────────────────
def test_env():
    print("\n" + "="*50)
    print("STEP 1 — Environment Variables")
    print("="*50)

    keys = ["SMTP_USER", "SMTP_PASSWORD", "EMAIL_FROM", "GROQ_API_KEY"]
    all_ok = True

    for key in keys:
        val = os.getenv(key)
        if val:
            # Mask sensitive values
            display = val[:4] + "*" * (len(val) - 4) if "PASSWORD" in key or "KEY" in key else val
            print(f"  ✅ {key} = {display}")
        else:
            print(f"  ❌ {key} = NOT SET")
            all_ok = False

    return all_ok


# ─────────────────────────────────────────────
# STEP 2 — Test LLM generates email content
# ─────────────────────────────────────────────
def test_llm_generation():
    print("\n" + "="*50)
    print("STEP 2 — LLM Email Generation (Groq)")
    print("="*50)

    try:
        from groq import Groq

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        fake_lead = {"company_name": "Cairo Test Restaurant"}

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{
                "role": "user",
                "content": f"""
                Write a short friendly cold sales email offering AI chatbot 
                services to {fake_lead['company_name']}.
                Keep it under 150 words. Be professional but human.
                
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

        print(f"  Raw LLM output:\n  {text[:200]}...")

        data = json.loads(text)
        print(f"\n  ✅ Subject: {data['subject']}")
        print(f"  ✅ Body preview: {data['body'][:100]}...")
        return data

    except Exception as e:
        print(f"  ❌ LLM generation failed: {e}")
        return None


# ─────────────────────────────────────────────
# STEP 3 — Test SMTP connection (no email sent)
# ─────────────────────────────────────────────
def test_smtp_connection():
    print("\n" + "="*50)
    print("STEP 3 — SMTP Connection Test (no email sent)")
    print("="*50)

    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")

    print(f"  Connecting to smtp.gmail.com:587")
    print(f"  Logging in as: {user}")
    print(f"  Password length: {len(password) if password else 0} chars")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        print("  ✅ Connected to Gmail SMTP")

        server.ehlo()
        server.starttls()
        print("  ✅ TLS started")

        server.login(user, password)
        print("  ✅ Login successful — credentials are VALID")

        server.quit()
        return True

    except smtplib.SMTPAuthenticationError as e:
        print(f"  ❌ Auth failed — bad credentials: {e}")
        print("\n  → Go to: https://myaccount.google.com/apppasswords")
        print("  → Generate a new App Password and update .env")
        return False

    except smtplib.SMTPConnectError as e:
        print(f"  ❌ Could not connect to Gmail SMTP: {e}")
        return False

    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return False


# ─────────────────────────────────────────────
# STEP 4 — Send a real test email to yourself
# ─────────────────────────────────────────────
def test_send_email(subject: str, body: str):
    print("\n" + "="*50)
    print("STEP 4 — Send Real Test Email")
    print("="*50)

    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    to_email = user  # send to yourself as a test

    print(f"  Sending to: {to_email}")
    print(f"  Subject: {subject}")

    try:
        msg = MIMEMultipart()
        msg["From"] = user
        msg["To"] = to_email
        msg["Subject"] = f"[AGENT3 TEST] {subject}"
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        server.starttls()
        server.login(user, password)
        server.sendmail(user, to_email, msg.as_string())
        server.quit()

        print(f"  ✅ Email sent! Check your inbox at {to_email}")
        return True

    except Exception as e:
        print(f"  ❌ Send failed: {e}")
        return False


# ─────────────────────────────────────────────
# STEP 5 — Qualify check simulation
# ─────────────────────────────────────────────
def test_qualification_logic():
    print("\n" + "="*50)
    print("STEP 5 — Qualification Logic Simulation")
    print("="*50)

    fake_leads = [
        {"company_name": "Cairo Bites", "email": "test@cairobites.com", "is_qualified": True},
        {"company_name": "No Email Co", "email": None, "is_qualified": True},
        {"company_name": "Already Has Bot", "email": "info@bot.com", "is_qualified": False},
    ]

    qualified = [l for l in fake_leads if l["is_qualified"] and l["email"]]

    print(f"  Total leads:     {len(fake_leads)}")
    print(f"  Qualified leads: {len(qualified)}")

    for lead in fake_leads:
        status = "✅ WILL EMAIL" if lead["is_qualified"] and lead["email"] else "⛔ SKIP"
        reason = "no email" if not lead["email"] else ("not qualified" if not lead["is_qualified"] else "")
        print(f"    {status} — {lead['company_name']} {f'({reason})' if reason else ''}")

    return qualified


# ─────────────────────────────────────────────
# RUN ALL TESTS
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 Agent 3 — Full Diagnostic Test")

    # Step 1
    env_ok = test_env()

    # Step 2
    email_content = test_llm_generation()

    # Step 3
    smtp_ok = test_smtp_connection()

    # Step 4 — only if SMTP works and LLM generated content
    if smtp_ok and email_content:
        test_send_email(email_content["subject"], email_content["body"])
    else:
        print("\n⚠️  Skipping real send — fix SMTP or LLM errors first")

    # Step 5
    test_qualification_logic()

    # Summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"  Env config:       {'✅' if env_ok else '❌'}")
    print(f"  LLM generation:   {'✅' if email_content else '❌'}")
    print(f"  SMTP connection:  {'✅' if smtp_ok else '❌'}")
    print("="*50)