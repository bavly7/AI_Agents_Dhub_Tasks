#!/usr/bin/env python3
"""
Quick test script to verify Gmail SMTP authentication
"""
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_gmail_connection():
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    print("=" * 60)
    print("Testing Gmail SMTP Authentication")
    print("=" * 60)
    print(f"📧 Email: {smtp_user}")
    print(f"🔑 Password: {'*' * len(smtp_password) if smtp_password else 'NOT SET'}")
    print("-" * 60)

    if not smtp_user or not smtp_password:
        print("❌ ERROR: Credentials not loaded from .env file!")
        print("   Make sure .env file exists in the project root")
        return False

    try:
        print("🔌 Connecting to smtp.gmail.com:587...")
        server = smtplib.SMTP("smtp.gmail.com", 587)

        print("🔒 Starting TLS...")
        server.starttls()

        print("🔐 Attempting login...")
        server.login(smtp_user, smtp_password)

        print("✅ SUCCESS! Authentication successful!")
        print("   Your Gmail SMTP credentials are working correctly.")

        server.quit()
        return True

    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ AUTHENTICATION FAILED!")
        print(f"   Error: {e}")
        print("\n💡 Common fixes:")
        print("   1. Enable 2-Factor Authentication on your Google account")
        print("   2. Generate a new App Password at:")
        print("      https://myaccount.google.com/apppasswords")
        print("   3. Make sure you're using the App Password, not your regular password")
        print("   4. Check if 'Less secure app access' needs to be enabled (if not using 2FA)")
        return False

    except Exception as e:
        print(f"❌ CONNECTION FAILED!")
        print(f"   Error: {e}")
        return False

if __name__ == "__main__":
    test_gmail_connection()
