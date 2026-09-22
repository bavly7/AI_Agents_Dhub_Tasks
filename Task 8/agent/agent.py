from langgraph.graph import StateGraph, END
from agent.nodes import (
    TicketState,
    classify_problem_node,
    classify_priority_node,
    create_tickets_node,
    end_node
)
from agent.edges import (
    should_continue_from_classify,
    route_after_priority,
    route_after_tickets
)


def create_support_agent():
    """
    Create and compile the LangGraph workflow for ticket routing.

    Flow:
    1. classify_problem -> checks if query is valid or NONE
    2. If NONE -> end
    3. If valid -> classify_priority
    4. create_tickets -> save to database
    5. end
    """
    # Initialize the graph
    workflow = StateGraph(TicketState)

    # Add nodes
    workflow.add_node("classify_problem", classify_problem_node)
    workflow.add_node("classify_priority", classify_priority_node)
    workflow.add_node("create_tickets", create_tickets_node)
    workflow.add_node("end", end_node)

    # Set entry point
    workflow.set_entry_point("classify_problem")

    # Add conditional edges
    workflow.add_conditional_edges(
        "classify_problem",
        should_continue_from_classify,
        {
            "classify_priority": "classify_priority",
            "end": "end"
        }
    )

    workflow.add_conditional_edges(
        "classify_priority",
        route_after_priority,
        {
            "create_tickets": "create_tickets"
        }
    )

    workflow.add_conditional_edges(
        "create_tickets",
        route_after_tickets,
        {
            "end": "end"
        }
    )

    # Add edge from end to END
    workflow.add_edge("end", END)

    # Compile the graph
    app = workflow.compile()

    return app


def process_ticket_request(query: str, name: str, email: str):
    """
    Process a ticket request through the LangGraph workflow.

    Args:
        query: User's support query
        name: User's name
        email: User's email

    Returns:
        dict: Result containing tickets or error message
    """
    app = create_support_agent()

    # Initial state
    initial_state = {
        "query": query,
        "name": name,
        "email": email,
        "problem_types": [],
        "priorities": [],
        "tickets": [],
        "is_none": False
    }

    # Run the workflow
    result = app.invoke(initial_state)

    # Format response
    if result["is_none"]:
        return {
            "success": False,
            "message": "Your query doesn't match our support categories. Please provide a valid support question."
        }

    return {
        "success": True,
        "message": f"Successfully created {len(result['tickets'])} ticket(s)",
        "tickets": result["tickets"]
    }
