# 🤖 AI Engineering Tasks & Agentic Systems

Welcome to the **AI Engineering Practice & Frameworks** repository!

This project showcases hands-on implementations of modern AI architectures, structured data extraction, autonomous tool-using agents, domain-specific LLM fine-tuning, Retrieval-Augmented Generation (RAG), conversational memory, multi-agent collaboration, and **AI-powered backend applications** using **LangChain, LangGraph, Pydantic, Hugging Face, FAISS, FastAPI, Streamlit, SQLite, and Groq**.

The repository demonstrates a progression from foundational LLM concepts toward **stateful, tool-using, database-connected, and user-facing AI applications**.

---

# 📌 Repository Overview

This repository serves as a showcase of practical AI engineering solutions designed to solve real-world automation, information processing, planning, and intelligent assistant challenges.

## Tasks

| Task                                                  | Description                                                                                                     |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Task 1: Structured Information Extractor**          | Enforcing strict schema outputs on unstructured candidate data                                                  |
| **Task 2: Autonomous Multi-Tool AI Agent**            | Building a stateful, tool-calling agent using LangGraph and custom APIs                                         |
| **Task 3: Domain-Specific LLM Fine-Tuning**           | Fine-tuning an open-source LLM for specialized medical customer support                                         |
| **Task 4: Simple RAG System**                         | Building a retriever and generator system using FAISS and PDF documents                                         |
| **Task 6: Advanced Conversational Memory Management** | Implementing stateful conversational memory with rolling summaries and persistent JSON storage                  |
| **🎬 Mid-Project: Movie Recommendation AI Assistant** | Full-stack RAG-powered conversational agent with watchlist management and personalized recommendations          |
| **Task 7: Multi-Agent Travel Planning System**        | Sequential multi-agent collaboration with conversational intake and specialized planning agents                 |
| **Task 8: Customer Support Ticket System**            | AI-powered customer support ticket routing using LangGraph, FastAPI, Groq, and SQLite                           |
| **Task 9: AI Wedding Planner Agent**                  | Tool-using wedding planning agent for searching and booking wedding halls with LangGraph, SQLite, and Streamlit |
| **🚀 Final Project: LeadFlow AI**                     | Autonomous 3-agent sales pipeline — discovers leads, qualifies them with AI, and sends personalized cold emails |

---

# ⚙️ Core Stack & Tools

| Category                   | Technologies                                       |
| -------------------------- | -------------------------------------------------- |
| **LLM Frameworks**         | LangChain, LangGraph                               |
| **Fine-Tuning & Training** | Hugging Face Transformers, PEFT, TRL, BitsAndBytes |
| **Vector Databases & RAG** | FAISS, HuggingFaceEmbeddings, PyPDF                |
| **Data Validation**        | Pydantic v2                                        |
| **LLM Engine**             | Groq — `openai/gpt-oss-120b`, Mistral 7B           |
| **Backend API**            | FastAPI                                            |
| **Frontend / UI**          | Streamlit                                          |
| **Databases**              | SQLite, JSON, Excel (XLSX)                         |
| **Geolocation**            | geopy, timezonefinder, pytz                        |
| **Environment Management** | python-dotenv                                      |
| **Language**               | Python                                             |

---

# 🎬 Mid-Project: Movie Recommendation AI Assistant with RAG

## 📋 Project Overview

An intelligent movie recommendation assistant that combines multiple AI concepts into a production-oriented conversational agent.

This project represents the culmination of several previously learned techniques:

* **RAG architecture**
* **LangChain agents**
* **FAISS vector search**
* **Conversational memory**
* **Tool orchestration**
* **Persistent user data**
* **Personalized recommendations**

## 🎯 Objective

Build a full-featured movie assistant that can:

1. **Search semantically** across 44,000+ movies using natural language
2. **Manage a personal watchlist** with Excel persistence
3. **Track viewing history** with ratings and notes
4. **Provide personalized recommendations**
5. **Maintain conversation context**
6. **Execute multi-step tasks** using ReAct agents

---

## 🚀 What I Built

### 🎥 Core Features

#### 1. Semantic Movie Search (RAG)

* **Dataset**: 44,503 movies from The Movie Database (TMDB)
* **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
* **Vector Store**: FAISS with 44,503 indexed documents
* **Search Capability**: Natural-language queries such as:

  * "mind-bending sci-fi movies"
  * "movies about dreams and reality"

#### 2. Watchlist Management System

* Add movies to a personal watchlist
* Mark movies as watched
* Store custom ratings
* Cancel/remove movies
* View filtered lists
* Persist data using Excel (`.xlsx`)

#### 3. Personalized Recommendations

* Analyzes watched movies and ratings
* Finds semantically similar movies
* Excludes movies already present in the watchlist
* Filters duplicate recommendations

#### 4. Conversational Memory

* Rolling 4-message memory window
* Full conversation backup
* Context-aware responses
* Session persistence through JSON

#### 5. Intelligent Agent with Tools

Six specialized tools:

* `search_movies`
* `add_to_watchlist`
* `mark_watched`
* `cancel_movie`
* `view_watchlist`
* `get_recommendations`

The agent follows a ReAct-style reasoning and tool-execution workflow.

#### 6. Interactive Validation

* Fuzzy movie title matching
* Alternative suggestions
* User confirmation for ambiguous titles
* Graceful error handling

#### 7. Performance Monitoring

* Response-time tracking
* Interaction logging
* Error logging
* Memory optimization

---

## 🏗️ Technical Architecture

```text
                    Movie Recommendation AI Assistant
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        ┌────────────┐      ┌────────────┐      ┌────────────┐
        │  RAG Core  │      │   Agent    │      │   Memory   │
        │   FAISS    │      │   ReAct    │      │   Manager  │
        └─────┬──────┘      └─────┬──────┘      └─────┬──────┘
              │                   │                   │
              ▼                   ▼                   ▼
        44K Movies             6 Tools            JSON Storage
        Vectorized             Executor            4 Messages
```

### Data Flow

```text
User Query
    ↓
Memory Manager
    ↓
ReAct Agent
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
┌─────────────────────────────────┐
│ FAISS Search                    │
│ Watchlist Operations            │
│ Recommendation Engine           │
└─────────────────────────────────┘
    ↓
Response Generation
    ↓
Memory Update
    ↓
User Response + Performance Log
```

---

# 🚀 Task 1: Structured Information Extractor

## 📋 Objective

Develop a reliable information extraction engine that transforms unstructured job applications, resumes, or self-introductions into strict, validated JSON formats without hallucinating missing information.

## 💡 Implementation Details

### 1. Schema Definition

Created a `Candidate` Pydantic `BaseModel` containing:

* `Candidate_name`
* `Years_of_experience`
* `Current_role`
* `Skills`
* `Highest_Education`

Pydantic ensures that extracted information follows the expected structure and data types.

### 2. Structured Parsing

Integrated LangChain's `PydanticOutputParser` to inject schema and formatting instructions into the LLM prompt.

### 3. Strict Guardrails

The extraction prompt instructs the model to:

* Never fabricate missing information
* Return `null` when information is unavailable
* Return `[]` when no skills are available
* Extract only information supported by the input

### 4. LCEL Chain

```text
PromptTemplate
      ↓
ChatGroq
      ↓
PydanticOutputParser
```

## 💻 Expected Output

```json
{
  "Candidate_name": "Bavly",
  "Years_of_experience": 3.0,
  "Current_role": "trainee",
  "Skills": [
    "ML",
    "CV applications",
    "AI agents"
  ],
  "Highest_Education": "Suez University"
}
```

---

# 🛠️ Task 2: Autonomous Multi-Tool AI Agent

## 📋 Objective

Build an AI agent capable of dynamically executing goals through multiple tools.

The agent interprets natural-language queries, selects appropriate tools, extracts parameters, interacts with databases and APIs, and maintains state through LangGraph.

## 🧰 Available Tools

### 📊 Analytics Tool

`analytics_tool`

Computes:

* Average
* Maximum
* Minimum
* Count

### 🌍 Location Information Tool

`location_tool`

Uses:

* geopy
* Nominatim API
* timezonefinder
* pytz

It can retrieve:

* Location
* Country
* Timezone
* Local time

### 📅 Schedule Management Tool

`scheduler_tool`

Uses SQLite to support:

* Event creation
* Event deletion
* Schedule management
* Conflict detection

---

## 🔄 LangGraph Workflow

```text
                 +-----------+
                 |   START   |
                 +-----+-----+
                       |
                       v
                +--------------+
                |  agent Node  |
                +------+-------+
                       |
                 tool_calls?
                   /       \
                Yes         No
                 /           \
                v             v
          +----------+      +-----+
          |  tools   |      | END |
          +----+-----+      +-----+
               |
               |
               +------------------+
                                  |
                                  v
                           +--------------+
                           |  agent Node  |
                           +--------------+
```

This creates an iterative workflow:

```text
User Request
     ↓
Agent Reasoning
     ↓
Tool Selection
     ↓
Tool Execution
     ↓
Tool Result
     ↓
Agent Re-evaluation
     ↓
Final Response
```

---

# 🚀 Task 3: Domain-Specific LLM Fine-Tuning

## 📋 Objective

Fine-tune an open-source LLM to specialize in answering domain-specific medical support questions.

## 💡 Implementation

### Model

```text
mistralai/Mistral-7B-Instruct-v0.3
```

Loaded using 4-bit quantization with `BitsAndBytesConfig`.

### Dataset

```text
FreedomIntelligence/medical-o1-reasoning-SFT
```

### Fine-Tuning

Used:

* PEFT
* LoRA
* Hugging Face Transformers
* TRL
* 4-bit quantization

| Parameter            | Value |
| -------------------- | ----- |
| Rank (`r`)           | 16    |
| Alpha                | 32    |
| Dropout              | 0.05  |
| Trainable Parameters | ~1.1% |
| Epochs               | 2     |

The resulting adapters and tokenizer configuration were saved locally.

> **Note:** The medical outputs demonstrated by the project are experimental model behavior and are not clinically validated medical advice.

---

# 📚 Task 4: Simple RAG System

## 📋 Objective

Build a Retrieval-Augmented Generation system capable of answering questions based only on a local PDF knowledge base.

## 📄 Document Processing

* 7 Parallel Computing PDFs
* Recursive character splitting
* Chunk size: `1000`
* Chunk overlap: `150`
* 56 resulting chunks

## 🔎 Vector Search

Embedding model:

```text
all-MiniLM-L6-v2
```

Vector store:

```text
FAISS
```

Index:

```text
Flat Index with L2 distance
```

Top 3 relevant chunks are retrieved for each question.

## 🤖 Generation

Groq:

```text
openai/gpt-oss-120b
```

The prompt instructs the model to refuse unsupported questions rather than hallucinate.

Example:

```text
Question:
How to bake a chocolate cake?

Answer:
I don't know, this information is not in the context.
```

---

# 🧠 Task 6: Advanced Conversational Memory Management

## 📋 Objective

Build a stateful conversational system that maintains useful context over long interactions while persisting conversation data.

## Features

* Rolling summaries
* Conversation history
* Persistent JSON storage
* Timestamps
* Session recovery
* OOP-based architecture

Main class:

```python
ConversationalAgent
```

Persistence methods:

```python
save_conversation()
load_conversation()
```

Example storage:

```json
{
  "conversation_history": [
    {
      "user": "Hi! My name is Bavly and I'm an AI engineer.",
      "assistant": "Hello Bavly! Nice to meet you.",
      "timestamp": "2026-09-14T13:54:19"
    }
  ],
  "summary": "User is an AI engineer working on AI projects."
}
```

---

# 🎬 Mid-Project: Movie Recommendation AI Assistant

The Mid-Project combines multiple previously learned concepts into a complete AI application.

### Concepts Combined

* RAG
* FAISS
* Agents
* Tools
* Memory
* Persistent storage
* Recommendation systems
* Fuzzy matching
* Logging
* Error handling

### Statistics

| Metric               | Value          |
| -------------------- | -------------- |
| Movies Indexed       | 44,503         |
| Vector Dimensions    | 384            |
| Index Build Time     | 124.43 seconds |
| Memory Window        | 4 messages     |
| Tools                | 6              |
| Max Agent Iterations | 3              |
| Search Time          | <100 ms        |

---

# ✈️ Task 7: Multi-Agent Travel Planning System

## 📋 Objective

Build an intelligent two-phase travel planning system combining conversational requirement gathering with sequential multi-agent collaboration.

## Phase 1: Intake Agent

Collects:

* Destination
* Budget
* Interests
* Duration

Uses:

```text
ConversationBufferWindowMemory(k=4)
```

## Phase 2: Multi-Agent Pipeline

Four specialized agents:

1. **Destination Agent**
2. **Budget Agent**
3. **Itinerary Agent**
4. **Recommendation Agent**

### Architecture

```text
User
 ↓
Intake Agent
 ↓
Requirements JSON
 ↓
Destination Agent
 ↓
Places & Activities JSON
 ↓
Budget Agent
 ↓
Cost Breakdown JSON
 ↓
Itinerary Agent
 ↓
Daily Schedule JSON
 ↓
Recommendation Agent
 ↓
Final Markdown Report
```

## Key Concepts

* Sequential multi-agent orchestration
* Specialized agent roles
* Structured data passing
* Conversational memory
* JSON output parsing
* Error-tolerant processing
* LangChain LCEL

---

# 🎫 Task 8: Customer Support Ticket System

## 📋 Objective

Build an AI-powered customer support ticket routing system using LangGraph, FastAPI, Groq, and SQLite.

## Features

* Problem classification
* Priority assignment
* Multi-issue detection
* UUID ticket generation
* Email-based retrieval
* SQLite persistence
* REST API

## Problem Categories

| Category      | Examples                                   |
| ------------- | ------------------------------------------ |
| **Technical** | System errors, bugs, outages               |
| **Billing**   | Payment issues, duplicate charges, refunds |
| **Account**   | Login, password, profile problems          |
| **General**   | Feature questions, how-to requests         |
| **NONE**      | Unsupported or off-topic queries           |

## Priority

| Priority   | Response Time |
| ---------- | ------------- |
| **HIGH**   | 2 hours       |
| **MEDIUM** | 24 hours      |
| **LOW**    | 48 hours      |

## Architecture

```text
Customer Query
      ↓
Problem Classification
      ↓
Is Problem NONE?
   /          \
 Yes           No
  ↓             ↓
END       Priority Classification
                ↓
          Ticket Creation
                ↓
          SQLite Database
                ↓
               END
```

## FastAPI Endpoints

| Method   | Endpoint                  | Purpose                    |
| -------- | ------------------------- | -------------------------- |
| **POST** | `/api/ticket`             | Create one or more tickets |
| **GET**  | `/api/tickets/{email}`    | Retrieve customer tickets  |
| **GET**  | `/api/tickets`            | Retrieve all tickets       |
| **GET**  | `/api/ticket/{ticket_id}` | Retrieve ticket by ID      |
| **GET**  | `/health`                 | API health check           |

---

# 💍 Task 9: AI Wedding Planner Agent

## 📋 Objective

Build an AI-powered wedding planning assistant that helps users **find and book wedding halls** through natural conversation.

The system combines:

* **LangGraph**
* **LangChain tool calling**
* **Groq**
* **Pydantic**
* **SQLite**
* **Streamlit**

The agent is designed to collect wedding requirements conversationally, search a local hall database, present available options, and complete a booking while checking date availability.

---

## 🎯 What I Built

The AI Wedding Planner provides two main capabilities:

### 1. 🔎 Wedding Hall Search

The agent collects the user's requirements:

* Number of guests
* Preferred hall style
* Food preference

It then calls:

```text
search_halls_tool
```

The tool searches the SQLite database for halls whose capacity can accommodate the requested number of guests.

### 2. 📅 Hall Booking

After the user selects a hall, the agent collects:

* Hall name
* Wedding date
* Customer name

It then calls:

```text
book_hall_tool
```

The booking tool checks whether the selected hall is already booked on the requested date before inserting the booking.

---

# 🏗️ Task 9 Architecture

```text
                         User
                           │
                           ▼
                 ┌──────────────────┐
                 │   Streamlit UI   │
                 │  Chat Interface  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    LangGraph     │
                 │   StateGraph     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    ChatGroq      │
                 │ gpt-oss-120b     │
                 └────────┬─────────┘
                          │
                    Tool Calls
                     /        \
                    /          \
                   ▼            ▼
        ┌────────────────┐  ┌────────────────┐
        │ Search Halls   │  │  Book Hall     │
        │     Tool       │  │     Tool       │
        └───────┬────────┘  └───────┬────────┘
                │                   │
                └─────────┬─────────┘
                          ▼
                  ┌───────────────┐
                  │    SQLite     │
                  │ wedding.db   │
                  └───────────────┘
```

---

# 🔄 LangGraph Workflow

The system uses a simple agentic loop.

```text
START
  ↓
LLM Node
  ↓
Does the LLM request a tool?
  │
  ├── No ──→ END
  │
  └── Yes
       ↓
    ToolNode
       ↓
    Tool Result
       ↓
    LLM Node
       ↓
    Final Response
```

The graph is created using:

```python
graph_builder = StateGraph(State)

graph_builder.add_node("llm", chatbot)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "llm")
graph_builder.add_conditional_edges("llm", tools_condition)
graph_builder.add_edge("tools", "llm")
```

This allows the LLM to decide when a database operation is required.

---

# 🧰 Task 9 Tools

## 🔎 `search_halls_tool`

The search tool accepts:

```python
capacity: int
style: str
food: str
```

Pydantic validation is provided through:

```python
SearchHallsInput
```

### Tool Workflow

```text
User Requirements
       ↓
LLM extracts:
capacity
style
food
       ↓
search_halls_tool
       ↓
SQLite Query
       ↓
Available Halls
       ↓
LLM
       ↓
User
```

The database query checks that the hall capacity is sufficient:

```sql
SELECT name, capacity, style, food, price
FROM halls
WHERE capacity >= ?
```

The tool then formats the results for the LLM.

---

# 📅 `book_hall_tool`

The booking tool accepts:

```python
hall_name: str
date: str
customer_name: str
```

The input is validated using:

```python
BookingDetails
```

## Booking Workflow

```text
Selected Hall
      ↓
Wedding Date
      ↓
Customer Name
      ↓
Check SQLite
      ↓
Is Date Available?
   /           \
 No             Yes
 ↓               ↓
ERROR          INSERT
 ↓               ↓
Ask for        SUCCESS
another date      ↓
              Confirm Booking
```

Before creating a booking, the system checks:

```sql
SELECT *
FROM bookings
WHERE hall_name = ?
AND date = ?
```

If a booking already exists:

```text
ERROR:
The hall is already booked on the requested date.
```

Otherwise, the system creates the booking:

```sql
INSERT INTO bookings
(hall_name, date, customer_name)
VALUES (?, ?, ?)
```

---

# 🧠 Pydantic Models

Task 9 uses Pydantic schemas to validate tool arguments.

## `SearchHallsInput`

```python
class SearchHallsInput(BaseModel):
    capacity: int = Field(
        description="Exact guest count as an integer."
    )

    style: str = Field(
        description="Preferred style."
    )

    food: str = Field(
        description="Food preferences as a single string."
    )
```

## `BookingDetails`

```python
class BookingDetails(BaseModel):
    hall_name: str = Field(
        description="The exact name of the hall to book"
    )

    date: str = Field(
        description="The date for the wedding"
    )

    customer_name: str = Field(
        description="The name of the customer booking the hall"
    )
```

This gives the LLM a structured schema for generating valid tool-call arguments.

---

# 💬 Conversational Workflow

The system is instructed to collect requirements **one by one** instead of assuming missing information.

The expected conversation flow is:

```text
AI:
Hello! How can I help you plan your wedding?

User:
I need a wedding hall.

AI:
How many guests are you expecting?

User:
250.

AI:
What type of hall style do you prefer?
For example: Indoor or Outdoor.

User:
Outdoor.

AI:
What are your food preferences?

User:
Egyptian food.

AI:
[Calls search_halls_tool]

AI:
I found these available halls:

- Royal Garden
- Nile Palace
- ...

Which hall would you like to book?
```

After the user chooses a hall:

```text
AI:
What date would you like to book it?

User:
2026-10-15

AI:
May I have your name?

User:
Bavly

AI:
[Calls book_hall_tool]

AI:
Congratulations! Your wedding hall has been booked successfully.
```

---

# 🛡️ Tool Error Handling

The system handles booking conflicts directly through tool results.

### Hall Already Booked

```text
ERROR:
The hall 'Royal Garden' is already booked on '2026-10-15'.
Ask the user to choose another date or a different hall.
```

The LLM receives this result and can continue the conversation by asking the user for another option.

### Successful Booking

```text
SUCCESS:
'Royal Garden' has been booked successfully
for Bavly on 2026-10-15.
```

The assistant then confirms the booking to the user.

---

# 🖥️ Streamlit User Interface

A Streamlit chat interface provides the user-facing application.

```text
┌──────────────────────────────────────────┐
│ 💍 AI Wedding Planner Agent              │
├──────────────────────────────────────────┤
│                                          │
│ 🤖 Hello! How can I help you?            │
│                                          │
│ 👤 I need a hall for 200 guests.         │
│                                          │
│ 🤖 What style do you prefer?             │
│                                          │
│ 👤 Outdoor                               │
│                                          │
│ 🤖 What food would you prefer?            │
│                                          │
│ 👤 Egyptian food                         │
│                                          │
├──────────────────────────────────────────┤
│ Type your message here...          [➤]   │
└──────────────────────────────────────────┘
```

The conversation is maintained using Streamlit's:

```python
st.session_state
```

The complete message history is passed back to the LangGraph agent so the assistant can maintain context throughout the booking process.

---

# 🗄️ SQLite Database

The application uses:

```text
wedding.db
```

The database contains information about wedding halls and bookings.

Conceptually, the system uses:

### `halls`

```text
name
capacity
style
food
price
```

### `bookings`

```text
hall_name
date
customer_name
```

The SQLite database provides persistent storage for available halls and completed bookings.

---

# 🔗 LangChain Tool Calling

The tools are registered using LangChain's `@tool` decorator:

```python
@tool(
    "search_halls_tool",
    args_schema=SearchHallsInput
)
def search_halls_tool(...):
    ...
```

and:

```python
@tool(
    "book_hall_tool",
    args_schema=BookingDetails
)
def book_hall_tool(...):
    ...
```

Both tools are then bound to the Groq LLM:

```python
tools = [
    search_halls_tool,
    book_hall_tool
]

llm = llm.bind_tools(
    tools,
    parallel_tool_calls=False
)
```

### Why disable parallel tool calls?

The wedding planning process is sequential:

```text
Collect requirements
       ↓
Search halls
       ↓
User chooses hall
       ↓
Collect date + name
       ↓
Book hall
```

The system therefore uses:

```python
parallel_tool_calls=False
```

to keep tool execution aligned with this conversational workflow.

---

# 🧩 LangGraph State

The graph maintains conversation messages using:

```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
```

The `add_messages` reducer allows new messages to be appended to the existing conversation state.

The graph therefore maintains:

```text
HumanMessage
      ↓
AIMessage
      ↓
ToolMessage
      ↓
AIMessage
      ↓
HumanMessage
      ↓
...
```

Internal tool messages are preserved for the agent but are not directly displayed in the Streamlit UI.

---

# 🎯 System Prompt Design

The agent is given explicit instructions defining the required workflow:

```text
1. Greet the user.
2. Ask for guest capacity.
3. Ask for preferred style.
4. Ask for food preferences.
5. Search halls after all criteria are available.
6. Present halls and prices.
7. Ask which hall to book.
8. Ask for date and customer name.
9. Check availability.
10. Confirm successful booking or request another option.
```

A key design principle is:

> **Do not assume missing information. Always ask the user.**

This prevents the agent from inventing booking requirements.

---

# 🛠️ Technical Challenges & Solutions

## Challenge 1: Maintaining Conversational Context

### Problem

The agent needs to remember previously collected requirements while the user provides information across multiple messages.

### Solution

The Streamlit application stores the message history in:

```python
st.session_state.messages
```

The complete message history is passed back to LangGraph for every interaction.

### Result

The agent can maintain context throughout the search and booking workflow.

---

## Challenge 2: Structured Tool Arguments

### Problem

The LLM needs to provide correctly formatted arguments when calling the database tools.

### Solution

Pydantic models are provided through `args_schema`:

```python
SearchHallsInput
BookingDetails
```

### Result

Tool arguments are explicitly structured and validated.

---

## Challenge 3: Booking Conflicts

### Problem

Two users should not be able to book the same hall on the same date.

### Solution

The booking tool performs an availability check before insertion:

```sql
SELECT *
FROM bookings
WHERE hall_name = ?
AND date = ?
```

Only available bookings are inserted.

### Result

The application prevents duplicate bookings for the same hall and date.

---

## Challenge 4: Sequential Tool Execution

### Problem

Searching for halls must happen before booking a specific hall.

### Solution

The LLM is instructed to follow a sequential workflow, and parallel tool calls are disabled.

```python
llm.bind_tools(
    tools,
    parallel_tool_calls=False
)
```

### Result

The booking process follows the expected business sequence.

---

## Challenge 5: Connecting an Agent to a User Interface

### Problem

A command-line agent is less convenient for an interactive customer workflow.

### Solution

A Streamlit chat interface was built around the LangGraph agent.

### Result

The AI workflow becomes an interactive conversational application.

---

# 📊 Task 9 System Specifications

| Component                  | Technology                          |
| -------------------------- | ----------------------------------- |
| **LLM Provider**           | Groq                                |
| **Model**                  | `openai/gpt-oss-120b`               |
| **Agent Framework**        | LangGraph                           |
| **LLM Framework**          | LangChain                           |
| **Tool Calling**           | LangChain Tools                     |
| **Data Validation**        | Pydantic                            |
| **Database**               | SQLite                              |
| **Frontend**               | Streamlit                           |
| **State Management**       | LangGraph + Streamlit Session State |
| **Environment Management** | python-dotenv                       |
| **Language**               | Python                              |

---

# 🧪 Example Scenarios

## Scenario 1: Search for a Hall

```text
User:
I need a hall for 300 guests.

AI:
What style do you prefer?

User:
Indoor.

AI:
What food would you prefer?

User:
Egyptian food.

AI:
[Calls search_halls_tool]

AI:
I found the following halls:
...
```

---

## Scenario 2: Successful Booking

```text
User:
I want to book Royal Palace.

AI:
What date would you like?

User:
2026-10-15.

AI:
May I have your name?

User:
Bavly Waleed.

AI:
[Calls book_hall_tool]

AI:
SUCCESS! Royal Palace has been booked
for Bavly Waleed on 2026-10-15.
```

---

## Scenario 3: Booking Conflict

```text
User:
Book Royal Palace for 2026-10-15.

AI:
[Calls book_hall_tool]

Tool:
ERROR: The hall is already booked on this date.

AI:
I'm sorry, Royal Palace is already booked on
2026-10-15. Would you like to choose another
date or another hall?
```

---

# 📁 Task 9 Project Structure

```text
Task 9 - AI Wedding Planner/
│
├── graph.py
│   # LangGraph workflow
│   # LLM configuration
│   # Tool definitions
│
├── models.py
│   # Pydantic tool schemas
│   # SearchHallsInput
│   # BookingDetails
│
├── app.py
│   # Streamlit chat interface
│
├── wedding.db
│   # SQLite database
│
├── requirements.txt
│   # Project dependencies
│
├── .env.example
│   # Environment variable template
│
└── README.md
    # Task documentation
```

---

# 🚀 How to Run Task 9

## 1. Install Dependencies

```bash
pip install langchain langchain-groq langchain-core langgraph
pip install pydantic python-dotenv streamlit
```

Or:

```bash
pip install -r requirements.txt
```

---

## 2. Configure API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never commit the actual API key.

---

## 3. Prepare the Database

Make sure:

```text
wedding.db
```

exists in the Task 9 directory and contains the required `halls` and `bookings` tables.

---

## 4. Start the Streamlit Application

From the Task 9 directory:

```bash
streamlit run app.py
```

The application will open in the browser.

---

# 🎓 Task 9 Learning Outcomes

This task demonstrates:

1. **Tool-Calling Agents** — Connecting an LLM to real database operations.
2. **LangGraph State Management** — Building an agentic workflow with graph-based execution.
3. **Conditional Tool Routing** — Using `tools_condition` to determine whether tools should execute.
4. **Structured Tool Inputs** — Using Pydantic schemas to validate LLM-generated arguments.
5. **Database-Connected AI** — Connecting an LLM agent to SQLite.
6. **Business Logic Integration** — Implementing real availability and booking rules.
7. **Conversational Workflow Design** — Collecting requirements progressively.
8. **Stateful UI** — Maintaining chat history through Streamlit session state.
9. **Error Handling** — Returning meaningful results for unavailable halls and booking conflicts.
10. **End-to-End AI Application Development** — Connecting LLM → Agent → Tools → Database → UI.

---

# 🔮 Potential Enhancements

Future improvements could include:

* [ ] Search by price range
* [ ] Search by exact food type
* [ ] Better style filtering
* [ ] Date availability search before selecting a hall
* [ ] Booking cancellation
* [ ] Booking modification
* [ ] Customer booking history
* [ ] Multiple wedding events per customer
* [ ] Authentication and user accounts
* [ ] PostgreSQL instead of SQLite
* [ ] FastAPI backend
* [ ] Admin dashboard
* [ ] Hall image previews
* [ ] Payment integration
* [ ] Email booking confirmations
* [ ] Calendar integration
* [ ] Multi-language support
* [ ] Deployment to a cloud platform

---

# 🗂️ Complete Project Structure

```text
.
├── Task 1/
│   ├── task1.ipynb
│   └── ...
│
├── Task 2 - langgraph/
│   ├── agent/
│   │   └── ...
│   ├── database/
│   │   └── schedule.db
│   ├── tools/
│   │   ├── analytics_tool
│   │   ├── location_tool
│   │   └── scheduler_tool
│   └── main.py
│
├── Task 3/
│   └── task3.ipynb
│
├── Task 4 - RAG/
│   ├── pdfs/
│   ├── faiss_parallel_computing_index/
│   └── task4.ipynb
│
├── Task 6 - Memory/
│   ├── agent_with_memory.ipynb
│   └── conversation_log.json
│
├── 🎬 Mid-Project - Movie Recommender/
│   ├── movie_recommender.ipynb
│   ├── data/
│   │   ├── movies_metadata.csv
│   │   └── credits.csv
│   ├── faiss_index/
│   ├── memory/
│   ├── logs/
│   └── my_watchlist.xlsx
│
├── Task 7 - Multi-Agent Travel Planner/
│   ├── multi_agent_travel_planner_final.ipynb
│   └── README.md
│
├── Task 8 - Customer Support Ticket System/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── nodes.py
│   │   ├── edges.py
│   │   └── agent.py
│   ├── database.py
│   ├── main.py
│   ├── test_api.py
│   ├── requirements.txt
│   └── .env.example
│
├── Task 9 - AI Wedding Planner/
│   ├── graph.py
│   ├── models.py
│   ├── app.py
│   ├── wedding.db
│   ├── requirements.txt
│   └── .env.example
│
├── 🚀 Final Project - LeadFlow AI/
│   ├── agents/
│   │   ├── agent1_prospector.py
│   │   ├── agent2_scraper.py
│   │   └── agent3_closer.py
│   ├── database/
│   │   ├── db.py
│   │   ├── models.py
│   │   └── leads.db
│   ├── tools/
│   │   └── email_tool.py
│   ├── tests/
│   │   ├── test_agent3.py
│   │   └── test_email_generation.py
│   ├── graph.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙️ Setup & Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Running the Projects

## Task 2: Multi-Tool Agent

```bash
cd "Task 2 - langgraph"
python main.py
```

## Task 8: Customer Support Ticket System

```bash
cd "Task 8 - Customer Support Ticket System"
python main.py
```

The API can be tested through:

```text
http://localhost:8000/docs
```

## Task 9: AI Wedding Planner

```bash
cd "Task 9 - AI Wedding Planner"
streamlit run app.py
```

## Final Project: LeadFlow AI

```bash
cd "Final Project - LeadFlow AI"
python main.py
```

## Jupyter Notebook Projects

For Tasks 1, 3, 4, 6, 7, and the Movie Recommendation project:

```bash
jupyter notebook
```

Then open the corresponding notebook.

---

# 🎯 Key Concepts Demonstrated

## LLM & Prompt Engineering

* LLM structured output
* Prompt engineering
* Guardrails
* LangChain Output Parsers
* LangChain Expression Language (LCEL)
* Format instructions
* Structured tool schemas

## Agentic AI

* LLM tool calling
* LangGraph `StateGraph`
* Conditional graph routing
* Stateful AI agents
* Multi-tool orchestration
* Agentic loops
* Tool execution
* ReAct pattern
* Sequential multi-agent pipelines
* Specialized agent roles
* Database-connected agents
* Autonomous end-to-end pipelines

## Vector Databases & Retrieval

* Document parsing
* Chunking
* Semantic search
* Embeddings
* FAISS
* Large-scale indexing
* RAG pipelines
* Anti-hallucination prompting
* Persistent vector stores

## Memory & State Management

* Rolling conversation summaries
* Token-efficient memory windows
* `ConversationBufferWindowMemory`
* LangGraph message state
* Streamlit session state
* JSON persistence
* Full conversation backups
* Context retention across agent calls

## Data & Backend Integration

* Pydantic validation
* Structured tool arguments
* SQLite
* FastAPI
* Streamlit
* External API integration
* Excel operations
* Schedule conflict detection
* ETL pipelines
* Fuzzy string matching
* Environment variable management
* Database-backed AI workflows
* SMTP email automation
* Web scraping pipelines

## LLM Fine-Tuning

* Parameter-Efficient Fine-Tuning
* LoRA
* 4-bit quantization
* Hugging Face Transformers
* SFTTrainer
* Domain-specific model adaptation

## Production Engineering

* Error handling
* Graceful degradation
* Retry logic
* Performance monitoring
* Logging
* Rate-limit management
* Data type compatibility
* API-specific workarounds
* Safe dictionary access
* Database persistence
* Business-rule validation
* Diagnostic test suites
* Environment path management

---

# 🧠 Complete Architecture Progression

The repository demonstrates a progression from foundational LLM concepts to increasingly complete AI applications:

```text
Structured Outputs
        ↓
Tool-Using Agents
        ↓
LLM Fine-Tuning
        ↓
RAG
        ↓
Conversational Memory
        ↓
Full AI Application
        ↓
Multi-Agent Collaboration
        ↓
Backend AI Systems
        ↓
Database-Connected AI Applications
        ↓
Autonomous AI Sales Agent
```

## 📈 Progression Timeline

1. **Task 1** — Structured data extraction
2. **Task 2** — Single agent with multiple tools
3. **Task 3** — Domain-specific LLM fine-tuning
4. **Task 4** — Knowledge retrieval with RAG
5. **Task 6** — Stateful conversation management
6. **Mid-Project** — Full RAG + Agent + Memory application
7. **Task 7** — Multi-agent collaboration
8. **Task 8** — AI-powered backend ticket system
9. **Task 9** — Database-connected conversational AI application
10. **Final Project** — Fully autonomous multi-agent sales pipeline

---

# 🔐 Security

API credentials and other secrets should always be stored in environment variables.

Example:

```env
GROQ_API_KEY=your_groq_api_key_here
SMTP_USER=your_gmail@gmail.com
SMTP_PASSWORD=your_app_password_here
EMAIL_FROM=your_gmail@gmail.com
```

Add sensitive files to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
*.zip

faiss_index/
logs/
memory/
my_watchlist.xlsx
conversation_log.json
*.db
```

Never commit:

* API keys
* Access tokens
* Passwords
* Database files containing sensitive user information
* Other credentials

---

# 🚀 Final Project: LeadFlow AI — Autonomous AI Sales Agent

## 📋 Project Overview

**LeadFlow AI** is a fully autonomous multi-agent sales automation system that finds business leads, qualifies them using AI, and sends personalized cold sales emails — all without human intervention.

The system combines:

* **LangGraph** multi-agent orchestration
* **Groq LLM** for qualification and email generation
* **Web scraping** for lead discovery and contact extraction
* **Pydantic** structured outputs
* **SQLite** persistent lead database
* **SMTP** automated email delivery
* **FastAPI** backend server

---

## 🎯 Objective

Build a production-oriented autonomous sales pipeline that:

1. **Discovers** business leads from the web using targeted search queries
2. **Scrapes** each lead's website to extract contact information
3. **Qualifies** leads using AI — checking if they are a good fit for the service
4. **Generates** personalized cold sales emails using an LLM
5. **Sends** those emails automatically via Gmail SMTP
6. **Tracks** all activity in a SQLite database

---

## 🤖 What I Built

### Three Specialized Agents

#### Agent 1 — Prospector
Searches the web for potential business leads based on a configurable search query (e.g., `"restaurants in Cairo Egypt"`). Returns a list of company names and URLs to investigate.

#### Agent 2 — Scraper & Qualifier
Visits each discovered URL, scrapes the website content, and uses the Groq LLM to:
- Extract the company's contact email
- Determine whether the company is a qualified lead (i.e., does not already have an AI chatbot)
- Return a structured qualification result using Pydantic

#### Agent 3 — Closer
For every qualified lead in the database:
- Calls the Groq LLM to write a personalized cold sales email offering AI chatbot services
- Sends the email via Gmail SMTP
- Marks the lead as emailed in the database

---

## 🏗️ Architecture

```text
                        LeadFlow AI
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
   │   Agent 1   │   │   Agent 2   │   │   Agent 3   │
   │ Prospector  │   │   Scraper   │   │   Closer    │
   │             │   │  Qualifier  │   │             │
   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
          │                  │                  │
          ▼                  ▼                  ▼
     Web Search          Groq LLM          Groq LLM
     Lead URLs         Qualification     Email Writer
                       + Extraction           │
                            │                  ▼
                            ▼            Gmail SMTP
                        SQLite DB        Email Sent
                       Lead Storage
```

---

## 🔄 LangGraph Workflow

```text
START
  ↓
run_prospector
  ↓
run_scraper
  ↓
Any qualified leads?
   /            \
 Yes             No
  ↓               ↓
run_closer        END
  ↓
END
```

The graph uses a **conditional edge** between the scraper and the closer — emails are only sent when qualified leads exist.

```python
def should_send_emails(state: AgentState) -> str:
    if len(state.get("qualified_leads", [])) > 0:
        return "run_closer"
    return END
```

---

## 🧰 Pydantic Models

### `Lead`

```python
class Lead(BaseModel):
    company_name: str
    url: str
    email: Optional[str] = None
    is_qualified: Optional[bool] = None
    email_sent: bool = False
    reason: Optional[str] = None
```

### `Qualifier`

```python
class Qualifier(BaseModel):
    is_qualified: bool
    extracted_email: Optional[str]
    reason: str
```

### `Closer`

```python
class Closer(BaseModel):
    subject: str
    body: str
```

---

## 📧 Email Generation

The Closer agent prompts the Groq LLM to write a personalized cold email for each qualified lead:

```text
- Signed by: "The LeadFlow AI Team"
- Highlights: 24/7 support, more bookings, instant FAQ handling
- CTA: "Let's connect — reply or book a free 15-min demo"
- Tone: confident, human, and compelling
- Length: under 150 words
```

Example generated output:

```
Subject: Boost Your Guest Experience with an AI Chatbot

Hi there,

I'm reaching out from LeadFlow AI because we noticed Cairo Bites
doesn't yet have an AI-powered chatbot — and we think it could
transform your guest experience.

Our chatbot handles reservations, answers menu questions, and
collects feedback 24/7, freeing your team to focus on what matters.
Setup takes under a week and requires zero coding on your end.

Restaurants using our solution have seen a measurable increase
in online bookings within the first month.

Let's connect — reply to this email or book a free 15-minute
demo to see it in action.

Best regards,
The LeadFlow AI Team
```

---

## 🗄️ SQLite Database

The system stores all lead activity in a persistent SQLite database:

### `leads` table

```text
id
company_name
url
email
is_qualified
email_sent
reason
created_at
```

Key operations:
- `save_lead()` — stores each discovered lead
- `get_qualified_leads()` — retrieves leads ready for outreach
- `mark_email_sent()` — marks a lead after successful delivery

---

## 📁 Project Structure

```text
Final Project - LeadFlow AI/
│
├── agents/
│   ├── agent1_prospector.py   # Web search & lead discovery
│   ├── agent2_scraper.py      # Website scraping & qualification
│   └── agent3_closer.py       # Email generation & sending
│
├── database/
│   ├── db.py                  # SQLite operations
│   ├── models.py              # Pydantic schemas & AgentState
│   └── leads.db               # SQLite database
│
├── tools/
│   └── email_tool.py          # Gmail SMTP email sender
│
├── tests/
│   ├── test_agent3.py         # Full Agent 3 diagnostic test
│   └── test_email_generation.py # Email content preview test
│
├── graph.py                   # LangGraph workflow definition
├── main.py                    # Entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ System Specifications

| Component            | Technology                  |
| -------------------- | --------------------------- |
| **LLM Provider**     | Groq                        |
| **Model**            | `openai/gpt-oss-120b`       |
| **Agent Framework**  | LangGraph                   |
| **Data Validation**  | Pydantic v2                 |
| **Database**         | SQLite                      |
| **Email Delivery**   | Gmail SMTP (smtplib)        |
| **Web Scraping**     | requests + BeautifulSoup    |
| **Backend**          | FastAPI                     |
| **Environment**      | python-dotenv               |
| **Language**         | Python                      |

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
SMTP_USER=your_gmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password
EMAIL_FROM=your_gmail@gmail.com
```

> Gmail requires a **16-character App Password** generated from [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) with 2-Step Verification enabled.

### 3. Run the Agent Pipeline

```bash
python main.py
```

### 4. Run Diagnostic Tests

```bash
# Test Agent 3 end-to-end (env, LLM, SMTP, send)
python tests/test_agent3.py

# Preview generated email content only
python tests/test_email_generation.py
```

---

## 🎓 Learning Outcomes

This final project demonstrates:

1. **Multi-Agent Orchestration** — Three specialized agents collaborating through LangGraph
2. **Conditional Graph Routing** — Skipping email delivery when no qualified leads exist
3. **Structured LLM Outputs** — Pydantic schemas for qualification and email generation
4. **Web Scraping Pipeline** — Automated contact extraction from business websites
5. **Database-Connected Agents** — SQLite persistence across the full pipeline
6. **SMTP Email Automation** — Programmatic email delivery via Gmail
7. **End-to-End AI Automation** — From web search to sent email with zero human input
8. **Diagnostic Testing** — Step-by-step test suite validating each system component
9. **Environment Management** — Robust `.env` loading across nested project directories
10. **Production-Oriented Design** — Error handling, lead tracking, and email state management

---

## 🔮 Potential Enhancements

* [ ] Add more target industries beyond restaurants
* [ ] LinkedIn scraping for additional contact discovery
* [ ] A/B testing different email templates
* [ ] Email open and reply tracking
* [ ] Streamlit dashboard for campaign monitoring
* [ ] Scheduling — run the pipeline daily automatically
* [ ] Multi-language email support
* [ ] CRM integration (HubSpot, Notion)
* [ ] Proxy rotation for large-scale scraping
* [ ] Deployment to a cloud platform

---

# 👨‍💻 Author

**Bavly Waleed**

AI Engineer | Machine Learning | Computer Vision | Agentic AI | Multi-Agent Systems

---

# ⭐ Project Purpose

This repository demonstrates the practical application of modern AI engineering concepts, moving beyond simple LLM prompting toward:

* Structured and validated LLM outputs
* Stateful AI agents
* Tool-using autonomous workflows
* External API integration
* Database-backed agents
* Parameter-efficient fine-tuning
* Domain-specific language models
* Large-scale RAG systems
* Local knowledge-base RAG
* Conversational memory
* Persistent session management
* Multi-agent collaboration
* Sequential agent pipelines
* AI-powered backend systems
* Database-connected AI applications
* Interactive conversational interfaces
* Autonomous end-to-end AI pipelines
* Production-oriented error handling

The overall progression demonstrates how modern AI systems can evolve from simple LLM interactions into **structured, autonomous, stateful, specialized, collaborative, and database-connected AI applications**.

The projects collectively demonstrate the complete AI engineering cycle:

```text
User
 ↓
Natural Language
 ↓
LLM
 ↓
Structured Decision
 ↓
Agent / Workflow
 ↓
Tools
 ↓
External Systems / Database
 ↓
Business Logic
 ↓
Validated Result
 ↓
User Interface / Automated Action
```

---

# 📝 License

This project is created for educational purposes as part of AI Engineering coursework.

---

**Last Updated:** October 1, 2026