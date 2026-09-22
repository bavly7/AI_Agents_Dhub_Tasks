from typing import TypedDict, List, Annotated
import operator
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
import json

# State definition for the graph
class TicketState(TypedDict):
    query: str
    name: str
    email: str
    problem_types: List[str]  # ✅ Replaces values
    priorities: List[str]
    tickets: List[dict]
    is_none: bool


def get_llm():
    """Initialize the LLM"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    return ChatGroq(
        api_key=api_key,
        model="openai/gpt-oss-120b",
        temperature=0
    )


def classify_problem_node(state: TicketState) -> TicketState:
    """
    Classify the problem type(s) from the user query.
    Can return multiple problem types or NONE.
    """
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a customer support classifier. Analyze the user's query and classify it into one or more of these categories:

**Problem Types:**
- Technical: System errors, bugs, service outages, technical issues
- Billing: Payment issues, charges, refunds, invoices
- Account: Login problems, password reset, account access, profile issues
- General: General questions, feature inquiries, how-to questions
- NONE: Query is not related to any support category (spam, gibberish, off-topic)

**Important Rules:**
1. A query can belong to MULTIPLE categories (e.g., "I can't login and was charged twice" = Account + Billing)
2. Return ONLY "NONE" if the query is completely unrelated to support
3. Be precise - don't overclassify

Return ONLY a JSON object with this format:
{{"problem_types": ["Technical", "Billing"]}}

Or if nothing matches:
{{"problem_types": ["NONE"]}}

Do not include any explanation, just the JSON."""),
        ("user", "Query: {query}")
    ])

    chain = prompt | llm
    response = chain.invoke({"query": state["query"]})

    # Parse the response
    try:
        result = json.loads(response.content)
        problem_types = result.get("problem_types", ["NONE"])
    except json.JSONDecodeError:
        # Fallback if LLM doesn't return valid JSON
        problem_types = ["General"]

    # Check if it's NONE
    is_none = "NONE" in problem_types

    return {
        **state,
        "problem_types": problem_types if not is_none else [],
        "is_none": is_none
    }


def classify_priority_node(state: TicketState) -> TicketState:
    """
    Classify the priority for each problem type detected.
    Returns a priority for each problem type.
    """
    llm = get_llm()
    problem_types = state["problem_types"]
    priorities = []

    for problem_type in problem_types:
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a priority classifier for customer support tickets.

**Priority Levels:**

HIGH:
- Complete service outage or system completely down
- Security breach or account compromise
- Money was accidentally withdrawn or critical payment errors
- Data loss or corruption

MEDIUM:
- Partial service disruption but workarounds exist
- Billing inquiries about charges
- Account access issues (password reset, can't login)
- Features not working but alternatives available

LOW:
- General questions about features
- Minor UI issues or cosmetic problems
- Documentation requests
- Non-urgent account updates or modifications

Analyze this query for the problem type "{problem_type}" and return ONLY the priority level: HIGH, MEDIUM, or LOW.

Return ONLY a JSON object:
{{"priority": "HIGH"}}

Do not include explanation."""),
            ("user", "Query: {query}")
        ])

        chain = prompt | llm
        response = chain.invoke({
            "query": state["query"],
            "problem_type": problem_type
        })

        try:
            result = json.loads(response.content)
            priority = result.get("priority", "MEDIUM")
        except json.JSONDecodeError:
            priority = "MEDIUM"  # Default fallback

        priorities.append(priority)

    return {
        **state,
        "priorities": priorities
    }


def create_tickets_node(state: TicketState) -> TicketState:
    """
    Create tickets in the database for each problem type + priority pair.
    """
    from database import db

    problem_types = state["problem_types"]
    priorities = state["priorities"]
    tickets = []

    # Estimated response times based on priority
    response_times = {
        "HIGH": "2 hours",
        "MEDIUM": "24 hours",
        "LOW": "48 hours"
    }

    for problem_type, priority in zip(problem_types, priorities):
        estimated_time = response_times.get(priority, "24 hours")

        ticket_id = db.create_ticket(
            name=state["name"],
            email=state["email"],
            query=state["query"],
            problem_type=problem_type,
            priority=priority,
            estimated_response_time=estimated_time
        )

        tickets.append({
            "ticket_id": ticket_id,
            "problem_type": problem_type,
            "priority": priority,
            "estimated_response_time": estimated_time
        })

    return {
        **state,
        "tickets": tickets
    }


def end_node(state: TicketState) -> TicketState:
    """Terminal node - no changes"""
    return state
