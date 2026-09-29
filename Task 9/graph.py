import sqlite3
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage
import os
from models import SearchHallsInput, BookingDetails
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


@tool("search_halls_tool", args_schema=SearchHallsInput)
def search_halls_tool(capacity: int, style: str, food: str) -> str:
    """Use this tool to search for wedding halls in the database based on user criteria.
    
    Args:
        capacity (int): A single integer for the guest count. If the user provides a range, use the highest number.
        style (str): The preferred style of the hall.
        food (str): The food preference combined into a single string.
    """
    conn = sqlite3.connect("wedding.db")
    cursor = conn.cursor()
    # Simple search logic: capacity should be enough, others can be loosely matched
    cursor.execute('''
        SELECT name, capacity, style, food, price 
        FROM halls 
        WHERE capacity >= ?
    ''', (capacity,))
    results = cursor.fetchall()
    conn.close()
    
    if not results:
        return "No exact matches found. Please tell the user we couldn't find a hall for this size and ask them to adjust criteria."
    
    formatted_results = "\n".join([f"- {r[0]} (Cap: {r[1]}, Style: {r[2]}, Food: {r[3]}) - Price: {r[4]} EGP" for r in results])
    return f"Available Halls:\n{formatted_results}"

@tool("book_hall_tool", args_schema=BookingDetails)
def book_hall_tool(hall_name: str, date: str, customer_name: str) -> str:
    """Use this tool to book a specific hall on a specific date for a customer."""
    conn = sqlite3.connect("wedding.db")
    cursor = conn.cursor()
    
    # Check availability
    cursor.execute('SELECT * FROM bookings WHERE hall_name = ? AND date = ?', (hall_name, date))
    conflict = cursor.fetchone()
    
    if conflict:
        conn.close()
        return f"ERROR: The hall '{hall_name}' is already booked on '{date}'. Ask the user to choose another date or a different hall."
        
    # Book the hall
    cursor.execute('''
        INSERT INTO bookings (hall_name, date, customer_name) 
        VALUES (?, ?, ?)
    ''', (hall_name, date, customer_name))
    conn.commit()
    conn.close()
    
    return f"SUCCESS: '{hall_name}' has been booked successfully for {customer_name} on {date}."

# 2. Setup LLM and Bind Tools
tools = [search_halls_tool, book_hall_tool]
# Replace with your Groq API key or ensure it's in env variables
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
        api_key=api_key,
        model="openai/gpt-oss-120b",
        temperature=0.3
    )
llm = llm.bind_tools(tools, parallel_tool_calls=False)
# 3. Define Graph State
class State(TypedDict):
    messages: Annotated[list, add_messages]

system_prompt = """You are a smart and friendly Wedding Planner AI.
Your goal is to help the user find and book a wedding hall. Follow these steps:
1. Greet the user and ask how you can help.
2. Ask for their requirements ONE BY ONE:
   - Number of guests (capacity)
   - Preferred style (Indoor, Outdoor, etc.)
   - Food preferences
3. Once you have all criteria, use the 'search_halls_tool'.
4. Present the available halls and their prices to the user. Ask which one they want to book, their preferred date, and their name.
5. Once they choose a hall, date, and provide their name, use the 'book_hall_tool'.
6. If the tool says ERROR (booked), apologize and ask them to pick another date or hall. If SUCCESS, congratulate them!
Do not assume any information, always ask the user."""

def chatbot(state: State):
    messages = state["messages"]
    # Ensure system prompt is always applied
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=system_prompt)] + messages
    response = llm.invoke(messages)
    return {"messages": [response]}

# 4. Build LangGraph
graph_builder = StateGraph(State)
graph_builder.add_node("llm", chatbot)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "llm")
graph_builder.add_conditional_edges("llm", tools_condition)
graph_builder.add_edge("tools", "llm")

agent_graph = graph_builder.compile()