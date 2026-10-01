from langgraph.graph import StateGraph, END
from agents.agent1_prospector import run_prospector
from agents.agent2_scraper import run_scraper
from agents.agent3_closer import run_closer
from database.models import AgentState

def should_send_emails(state: AgentState) -> str:
    if len(state.get("qualified_leads", [])) > 0:
        return "run_closer"
    return END

def build_graph():
    graph = StateGraph(AgentState)

    # add nodes
    graph.add_node("run_prospector", run_prospector)
    graph.add_node("run_scraper", run_scraper)
    graph.add_node("run_closer", run_closer)

    # add edges
    graph.set_entry_point("run_prospector")
    graph.add_edge("run_prospector", "run_scraper")

    # conditional edge — only email if qualified leads exist
    graph.add_conditional_edges(
        "run_scraper",
        should_send_emails,
        {
            "run_closer": "run_closer",
            END: END
        }
    )

    graph.add_edge("run_closer", END)

    return graph.compile()