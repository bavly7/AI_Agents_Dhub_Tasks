from langchain.agents import create_agent
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from typing import Literal


from tools.analytics import simple_analytics_tool, AnalyticsInput
from tools.location import location_info_tool, LocationInput
from tools.scheduler import schedule_management_tool
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file



@tool(args_schema=AnalyticsInput)
def analytics_tool(numbers: list[float]):
    """Computes average, max, min, and count of a list of numbers."""
    return simple_analytics_tool(numbers)

@tool(args_schema=LocationInput)
def location_tool(location_name: str):
    """Returns country, timezone, and current local time for a given location."""
    return location_info_tool(location_name)


class SchedulerInput(BaseModel):
    action: str = Field(description="Must be 'create' or 'delete'")
    event_name: str = Field(default=None, description="Name of the event (e.g., 'Team Meeting')")
    date: str = Field(default=None, description="Date in YYYY-MM-DD format")
    time: str = Field(default=None, description="Time in HH:MM format")

@tool(args_schema=SchedulerInput)
def scheduler_tool(action: str, event_name: str = None, date: str = None, time: str = None):
    """Manages scheduling events: create, update, delete, and checks for conflicts."""
    return schedule_management_tool(action, event_name, date, time)


tools_list = [analytics_tool, location_tool, scheduler_tool]






llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0) 


# Bind the tools to the LLM so it knows what capabilities are available
llm_with_tools = llm.bind_tools(tools_list)

# ---------------------------------------------------------
# 3. Custom System Prompt (The Agent's Behavioral Catalog)
# ---------------------------------------------------------
CUSTOM_SYSTEM_PROMPT = SystemMessage(
    content="""You are an advanced, helpful, and strict AI Assistant. 
    You have access to specific tools: analytics, location, and scheduler.
    
    - If the user request matches a tool, use it and extract the required parameters carefully.
    - **For the analytics tool:** If the user asks for a specific metric (like average, max, min, or count only), make sure to pass the `operation` parameter accordingly (e.g., 'average', 'maximum', 'minimum', 'count'). If they want general stats, leave it as 'all'.
    - If required parameters are missing (like time for scheduling or numbers for analytics), ask the user to provide them politely.
    - If the request is completely out of your tools' scope, politely say 'I don't know' or explain what you can do.
    - Always verify results before giving the final answer to the user."""
)

# ---------------------------------------------------------
# 4. Defining the Nodes (The Processing Units)
# ---------------------------------------------------------

def call_model(state: MessagesState):
    """
    Node 1: The Agent Node.
    Combines the custom system prompt with the ongoing message history 
    and invokes the tool-bound LLM to decide the next action.
    """
    messages = [CUSTOM_SYSTEM_PROMPT] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# Pre-built LangGraph ToolNode handles executing the tool requested by the LLM
tools_node = ToolNode(tools_list)

# ---------------------------------------------------------
# 5. Defining Routing Logic & Edges (The Flow Control)
# ---------------------------------------------------------

def should_continue(state: MessagesState) -> str:
    """
    Conditional Edge Router:
    Inspects the latest message to check if the LLM requested a tool call.
    - If yes -> routes to the 'tools' node.
    - If no -> terminates the loop ('END') and outputs the response to the user.
    """
    messages = state["messages"]
    last_message = messages[-1]
    
    if last_message.tool_calls:
        return "tools"
    return END

# ---------------------------------------------------------
# 6. Assembling the StateGraph (The Complete Workflow)
# ---------------------------------------------------------

# Initialize the workflow graph using LangGraph's standard MessagesState
workflow = StateGraph(MessagesState)

# Step A: Add nodes to the graph
workflow.add_node("agent", call_model)
workflow.add_node("tools", tools_node)

# Step B: Define entry point (Start -> Agent)
workflow.add_edge(START, "agent")

# Step C: Add conditional routing from the agent node
workflow.add_conditional_edges("agent", should_continue)

# Step D: Create the loop (Tools results must flow back to the agent for evaluation)
workflow.add_edge("tools", "agent")

# Step E: Compile the workflow into a runnable app
graph_app = workflow.compile()