from agent.nodes import TicketState

def should_continue_from_classify(state: TicketState) -> str:
    """
    Decides the next node after problem classification.
    If NONE -> go to end
    If valid problem types -> go to priority classification
    """
    if state.get("is_none", False):
        return "end"
    else:
        return "classify_priority"


def route_after_priority(state: TicketState) -> str:
    """
    After priority classification, always go to create tickets.
    """
    return "create_tickets"


def route_after_tickets(state: TicketState) -> str:
    """
    After creating tickets, end the workflow.
    """
    return "end"
