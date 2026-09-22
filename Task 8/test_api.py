import requests
import json
from typing import Dict, List

# Base URL for the API
BASE_URL = "http://localhost:8000"


def print_response(response: requests.Response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"{'='*60}")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)
    print(f"{'='*60}\n")


def test_root():
    """Test the root endpoint"""
    print("🧪 Testing Root Endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print_response(response)


def test_health():
    """Test health check"""
    print("🧪 Testing Health Check...")
    response = requests.get(f"{BASE_URL}/health")
    print_response(response)


def test_create_ticket(query: str, name: str, email: str):
    """Test creating a ticket"""
    print(f"🧪 Testing Ticket Creation...")
    print(f"Query: {query}")
    print(f"Name: {name}")
    print(f"Email: {email}")

    data = {
        "query": query,
        "name": name,
        "email": email
    }

    response = requests.post(f"{BASE_URL}/api/ticket", json=data)
    print_response(response)
    return response.json() if response.status_code == 200 else None


def test_get_tickets_by_email(email: str):
    """Test retrieving tickets by email"""
    print(f"🧪 Testing Get Tickets by Email: {email}")
    response = requests.get(f"{BASE_URL}/api/tickets/{email}")
    print_response(response)


def test_get_all_tickets():
    """Test retrieving all tickets"""
    print("🧪 Testing Get All Tickets...")
    response = requests.get(f"{BASE_URL}/api/tickets")
    print_response(response)


def run_all_tests():
    """Run comprehensive test suite"""
    print("\n" + "="*60)
    print("🚀 CUSTOMER SUPPORT TICKET SYSTEM - TEST SUITE")
    print("="*60 + "\n")

    # Test 1: Basic endpoints
    test_root()
    test_health()

    # Test 2: Single problem type (Account issue - HIGH priority)
    print("\n" + "🔵"*30)
    print("TEST CASE 1: Single Problem - Account Access (HIGH)")
    print("🔵"*30)
    test_create_ticket(
        query="I can't login to my account and I think someone hacked it!",
        name="Alice Johnson",
        email="alice@example.com"
    )

    # Test 3: Single problem type (Billing - MEDIUM priority)
    print("\n" + "🔵"*30)
    print("TEST CASE 2: Single Problem - Billing Question (MEDIUM)")
    print("🔵"*30)
    test_create_ticket(
        query="I have a question about my last invoice. Can you explain the charges?",
        name="Bob Smith",
        email="bob@example.com"
    )

    # Test 4: Single problem type (General - LOW priority)
    print("\n" + "🔵"*30)
    print("TEST CASE 3: Single Problem - General Question (LOW)")
    print("🔵"*30)
    test_create_ticket(
        query="How do I change my profile picture?",
        name="Carol White",
        email="carol@example.com"
    )

    # Test 5: Multiple problem types (Account + Billing)
    print("\n" + "🔵"*30)
    print("TEST CASE 4: Multiple Problems - Account + Billing")
    print("🔵"*30)
    test_create_ticket(
        query="I can't access my account and I was charged twice for the same service!",
        name="David Brown",
        email="david@example.com"
    )

    # Test 6: Multiple problem types (Technical + Account + Billing)
    print("\n" + "🔵"*30)
    print("TEST CASE 5: Multiple Problems - Technical + Account + Billing")
    print("🔵"*30)
    test_create_ticket(
        query="The entire system is down, I can't login, and I see duplicate charges on my card!",
        name="Eve Davis",
        email="eve@example.com"
    )

    # Test 7: NONE case (spam/off-topic)
    print("\n" + "🔵"*30)
    print("TEST CASE 6: Invalid Query (NONE)")
    print("🔵"*30)
    test_create_ticket(
        query="Hello! Check out this great deal on watches!",
        name="Spammer McSpam",
        email="spam@example.com"
    )

    # Test 8: Technical issue (HIGH priority)
    print("\n" + "🔵"*30)
    print("TEST CASE 7: Technical Issue - Service Outage (HIGH)")
    print("🔵"*30)
    test_create_ticket(
        query="Your entire service is down! I can't access anything and losing business!",
        name="Frank Miller",
        email="frank@example.com"
    )

    # Test 9: Retrieve tickets by specific email
    print("\n" + "🔵"*30)
    print("TEST CASE 8: Retrieve Tickets for david@example.com")
    print("🔵"*30)
    test_get_tickets_by_email("david@example.com")

    # Test 10: Retrieve all tickets
    print("\n" + "🔵"*30)
    print("TEST CASE 9: Retrieve All Tickets")
    print("🔵"*30)
    test_get_all_tickets()

    print("\n" + "="*60)
    print("✅ TEST SUITE COMPLETED")
    print("="*60 + "\n")


def interactive_test():
    """Interactive testing mode"""
    print("\n" + "="*60)
    print("🎯 INTERACTIVE TESTING MODE")
    print("="*60 + "\n")

    while True:
        print("\nOptions:")
        print("1. Create a ticket")
        print("2. Get tickets by email")
        print("3. Get all tickets")
        print("4. Run full test suite")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            query = input("Enter query: ").strip()
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            test_create_ticket(query, name, email)

        elif choice == "2":
            email = input("Enter email: ").strip()
            test_get_tickets_by_email(email)

        elif choice == "3":
            test_get_all_tickets()

        elif choice == "4":
            run_all_tests()

        elif choice == "5":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    import sys

    print("\n" + "🎯"*30)
    print("CUSTOMER SUPPORT TICKET SYSTEM - API TESTER")
    print("🎯"*30 + "\n")

    print("Make sure the server is running at http://localhost:8000")
    print("Start it with: python main.py\n")

    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive_test()
    else:
        print("Running automated test suite...")
        print("(Use 'python test_api.py interactive' for interactive mode)\n")
        run_all_tests()
