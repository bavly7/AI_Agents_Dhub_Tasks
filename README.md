# 🤖 AI Engineering Tasks & Agentic Systems

Welcome to the **AI Engineering Practice & Frameworks** repository!

This project showcases hands-on implementations of modern LLM architectures, structured data extraction, autonomous multi-tool AI agents, domain-specific LLM fine-tuning, Retrieval-Augmented Generation (RAG), conversational memory management, and **multi-agent collaboration systems** using **LangChain, LangGraph, Pydantic, Hugging Face, FAISS, PEFT, and Groq**.

---

## 📌 Repository Overview

This repository serves as a showcase of practical AI engineering solutions designed to solve real-world automation and intelligent processing challenges.

### Tasks

| Task | Description |
|------|-------------|
| **Task 1: Structured Information Extractor** | Enforcing strict schema outputs on unstructured candidate data |
| **Task 2: Autonomous Multi-Tool AI Agent** | Building a stateful, tool-calling agent using LangGraph and custom APIs |
| **Task 3: Domain-Specific LLM Fine-Tuning** | Fine-tuning an open-source LLM for specialized medical customer support |
| **Task 4: Simple RAG System** | Building a retriever and generator system using FAISS and PDF documents |
| **Task 6: Advanced Conversational Memory Management** | Implementing stateful conversational memory with rolling summaries and persistent JSON storage |
| **🎬 Mid-Project: Movie Recommendation AI Assistant** | Full-stack RAG-powered conversational agent with watchlist management and personalized recommendations |
| **Task 7: Multi-Agent Travel Planning System** | Sequential multi-agent collaboration with conversational intake and specialized planning agents |
| **Task 8: Customer Support Ticket System** | AI-powered customer support ticket routing using LangGraph, FastAPI, Groq, and SQLite |


---

## ⚙️ Core Stack & Tools

| Category | Technologies |
|----------|--------------|
| **LLM Frameworks** | LangChain, LangGraph |
| **Fine-Tuning & Training** | Hugging Face Transformers, PEFT, TRL, BitsAndBytes |
| **Vector Databases & RAG** | FAISS, HuggingFaceEmbeddings, PyPDF |
| **Data Validation** | Pydantic v2 |
| **LLM Engine** | Groq — `openai/gpt-oss-120b`, Mistral 7B |
| **Geolocation** | geopy, timezonefinder, pytz |
| **Database** | SQLite, JSON, Excel (XLSX) |
| **Environment Management** | python-dotenv |
| **Language** | Python |

---

# 🎬 Mid-Project: Movie Recommendation AI Assistant with RAG

## 📋 Project Overview

An intelligent movie recommendation assistant that combines multiple AI concepts into a production-ready conversational agent. This project represents the culmination of all previously learned techniques: **RAG architecture**, **LangChain agents**, **FAISS vector search**, **conversational memory**, and **tool orchestration**.

## 🎯 Objective

Build a full-featured movie assistant that can:

1. **Search semantically** across 44,000+ movies using natural language
2. **Manage a personal watchlist** with Excel persistence
3. **Track viewing history** with ratings and notes
4. **Provide personalized recommendations** based on watch history
5. **Maintain conversation context** with memory management
6. **Execute multi-step tasks** autonomously using ReAct agents

---

## 🚀 What I Built

### 🎥 **Core Features**

#### 1. **Semantic Movie Search (RAG)**
- **Dataset**: 44,503 movies from The Movie Database (TMDB)
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Store**: FAISS with 44,503 indexed documents
- **Search Capability**: Natural language queries like "mind-bending sci-fi movies" or "movies about dreams and reality"

#### 2. **Watchlist Management System**
- **Add movies** to a personal watchlist with validation
- **Mark as watched** with custom ratings (e.g., "8/10")
- **Cancel/remove** movies from the list
- **View filtered lists** by status (Want to Watch, Watched, Cancelled)
- **Persistence**: Excel (.xlsx) format for easy manual access

#### 3. **Personalized Recommendations**
- Analyzes user's watch history and ratings
- Recommends similar movies **not already in the watchlist**
- Uses semantic similarity based on liked movies
- Filters out duplicates automatically

#### 4. **Conversational Memory**
- **Rolling window memory**: Keeps last 4 messages to prevent token overflow
- **Full conversation backup**: All interactions saved to JSON
- **Context-aware responses**: Agent remembers previous queries
- **Session persistence**: Can resume conversations after restart

#### 5. **Intelligent Agent with Tools**
- **ReAct Agent Pattern**: Thinks, acts, observes, and responds
- **6 Specialized Tools**:
  - `search_movies`: Semantic search across movie database
  - `add_to_watchlist`: Add movies with fuzzy matching
  - `mark_watched`: Track viewing history with ratings
  - `cancel_movie`: Remove unwanted movies
  - `view_watchlist`: Display current watchlist
  - `get_recommendations`: Generate personalized suggestions

#### 6. **Interactive Validation**
- **Fuzzy matching**: Suggests alternatives when exact title not found
- **User confirmation**: Asks "Did you mean X?" for ambiguous queries
- **Graceful error handling**: Falls back to simple responses on failures

#### 7. **Performance Monitoring & Logging**
- Response time tracking for each query
- Complete interaction logging to `logs/session.log`
- Memory usage optimization (4-message window)
- Error logging for debugging

---

## 🏗️ Technical Architecture

### **System Components**

```text
┌────────────────────────────────────────────────────────┐
│          Movie Recommendation AI Assistant              │
└────────────────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   RAG Core   │  │   Agent      │  │   Memory     │
│   (FAISS)    │  │   (ReAct)    │  │   Manager    │
└──────────────┘  └──────────────┘  └──────────────┘
        │                │                │
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  44K Movies  │  │   6 Tools    │  │ JSON Storage │
│  Vectorized  │  │   Executor   │  │ 4-msg Window │
└──────────────┘  └──────────────┘  └──────────────┘
```

### **Data Flow**

```text
User Query
    ↓
Memory Manager (Load Context)
    ↓
ReAct Agent (Reasoning)
    ↓
Tool Selection & Execution
    ↓
┌─────────────────────────────────┐
│  FAISS Search                   │  ← Semantic Retrieval
│  Watchlist Operations           │  ← Excel CRUD
│  Recommendation Engine          │  ← History Analysis
└─────────────────────────────────┘
    ↓
Response Generation
    ↓
Memory Update (Save Context)
    ↓
User Response + Performance Log
```

---

## 💡 Implementation Highlights

### **1. Data Processing Pipeline**

```python
# Loaded 45,466 movies → Cleaned to 44,503
# ✓ Removed movies without plots
# ✓ Parsed JSON genres from strings
# ✓ Extracted directors and top 5 cast members
# ✓ Merged credits with metadata
# ✓ Created rich document representations
```

**Document Format:**
```text
Toy Story (1995)
Genre: Animation, Comedy, Family
Director: John Lasseter
Cast: Tom Hanks, Tim Allen, Don Rickles, Jim Varney, Wallace Shawn
Rating: 7.7/10

Plot: Led by Woody, Andy's toys live happily in his room until...
```

### **2. Vector Store Creation**

```python
# Created 44,503 LangChain Documents
# Embedded using all-MiniLM-L6-v2 (384 dimensions)
# Indexed with FAISS in 124.43 seconds
# Saved to disk for fast loading
```

### **3. Memory Optimization**

```python
class MemoryManager:
    """Strict 4-message window to avoid rate limits"""
    
    def __init__(self, max_recent=4):
        self.max_recent = 4  # 2 conversation pairs
        self.memory = {'recent_messages': []}
    
    def add_message(self, role, content):
        # Truncate long messages to 800 chars
        # Keep ONLY last 4 messages
        # No LLM summarization needed!
        if len(self.memory['recent_messages']) > 4:
            self.memory['recent_messages'] = 
                self.memory['recent_messages'][-4:]
```

**Why 4 messages?**
- Prevents Groq rate limit errors
- Eliminates need for expensive LLM summarization
- Maintains immediate conversation context
- Full backup saved separately for recovery

### **4. Watchlist Manager with Error Handling**

```python
class WatchlistManager:
    """Excel-based watchlist with fuzzy matching"""
    
    def add_to_watchlist(self, movie_name: str):
        # 1. Fuzzy search in movie database
        # 2. Return suggestions if no exact match
        # 3. Check for duplicates in watchlist
        # 4. Add with metadata (genre, year, etc.)
        # 5. Handle file permission errors gracefully
        
    def mark_watched(self, movie_name: str, rating: str):
        # 1. Find movie in watchlist
        # 2. Update status to "Watched"
        # 3. Record timestamp
        # 4. Save rating (if provided)
        # 5. Retry logic for file locks
```

### **5. ReAct Agent Configuration**

```python
# Tools → Agent → Executor
tools = [
    Tool(name="search_movies", ...),
    Tool(name="add_to_watchlist", ...),
    Tool(name="mark_watched", ...),
    Tool(name="cancel_movie", ...),
    Tool(name="view_watchlist", ...),
    Tool(name="get_recommendations", ...)
]

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,  # Prevent infinite loops
    handle_parsing_errors=True
)
```

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Movies Indexed** | 44,503 |
| **Vector Dimensions** | 384 (MiniLM-L6-v2) |
| **Index Build Time** | 124.43 seconds |
| **Memory Window** | 4 messages (2 pairs) |
| **Tools Available** | 6 specialized functions |
| **Max Agent Iterations** | 3 per query |
| **Avg Response Time** | 2-7 seconds |
| **Storage Format** | Excel (watchlist), JSON (memory) |

---

## 🎯 Key Concepts Demonstrated

### **Advanced RAG Implementation**
- ✅ Large-scale document indexing (44K+ items)
- ✅ Semantic search with FAISS
- ✅ Document chunking and metadata preservation
- ✅ Persistent vector store for fast loading

### **Agentic AI Patterns**
- ✅ ReAct (Reasoning + Acting) agent architecture
- ✅ Multi-tool orchestration
- ✅ Dynamic tool selection based on intent
- ✅ Iterative reasoning loops with max_iterations safety

### **Memory Management**
- ✅ Rolling window memory (4-message optimization)
- ✅ Conversation history persistence
- ✅ Full backup system for recovery
- ✅ Token-efficient context management

### **Production Engineering**
- ✅ Error handling and graceful degradation
- ✅ Performance monitoring and logging
- ✅ File lock retry logic
- ✅ Interactive user validation
- ✅ Fuzzy matching for user input
- ✅ Data type conversion handling (Excel compatibility)

---

## 💻 Sample Interactions

### **Example 1: Semantic Search**

```text
You: What are some mind-bending sci-fi movies?

Bot: Found movies:

1. Inception (2010)
   Science Fiction, Thriller | 9.0/10
   A thief who steals corporate secrets through dream-sharing...

2. Interstellar (2014)
   Science Fiction, Drama | 8.6/10
   Explores time dilation and black holes in space exploration...

3. The Matrix (1999)
   Science Fiction, Action | 8.7/10
   A computer hacker learns about the true nature of reality...
```

### **Example 2: Watchlist Management**

```text
You: Add Inception to my watchlist

Bot: ✅ Added 'Inception' (2010) to your watchlist!

You: I watched Inception and loved it! Rate it 9/10

Bot: ✅ Marked 'Inception' as watched!

You: Give me recommendations

Bot: Based on what you've watched, try:

1. Interstellar (2014)
   Science Fiction, Drama | 8.6/10

2. Shutter Island (2010)
   Mystery, Thriller | 8.2/10

3. The Prestige (2006)
   Drama, Mystery, Science Fiction | 8.5/10
```

### **Example 3: Interactive Validation**

```text
You: Add intersteller to my list

Bot: I couldn't find that exact movie. Did you mean 'Interstellar'? 
(Please reply Yes or No)

You: Yes

Bot: ✅ Added 'Interstellar' (2014) to your watchlist!
```

---

## 🛠️ Technical Challenges Solved

### **Challenge 1: Groq Rate Limits**
**Problem**: Long conversation history caused rate limit errors  
**Solution**: Implemented strict 4-message rolling window, eliminated LLM-based summarization

### **Challenge 2: Excel File Locking**
**Problem**: `PermissionError` when watchlist file is open  
**Solution**: Added retry logic with exponential backoff + user-friendly error messages

### **Challenge 3: Agent Infinite Loops**
**Problem**: Agent sometimes repeated tool calls unnecessarily  
**Solution**: Set `max_iterations=3` and improved prompt formatting instructions

### **Challenge 4: Fuzzy Movie Title Matching**
**Problem**: Users might misspell movie titles  
**Solution**: Implemented partial string matching + interactive confirmation system

### **Challenge 5: Excel Data Type Errors**
**Problem**: DateTime/Rating columns caused dtype errors when updating  
**Solution**: Explicitly convert columns to `object` type before assignment

---

## 📁 Project File Structure

```text
movie_recommender/
│
├── movie_recommender.ipynb          # Main implementation notebook
├── README.md                        # This file
│
├── data/
│   ├── movies_metadata.csv          # 45,466 movies (raw)
│   └── credits.csv                  # Cast and crew data
│
├── faiss_index/                     # Persisted vector store
│   ├── index.faiss                  # FAISS index file
│   └── index.pkl                    # Metadata pickle
│
├── memory/
│   ├── conversation_memory.json     # 4-message window storage
│   └── full_backup.json             # Complete conversation history
│
├── logs/
│   └── session.log                  # Performance and error logs
│
├── my_watchlist.xlsx                # User's movie watchlist
│
└── .env                             # GROQ_API_KEY configuration
```

---

## 🚀 How to Run

### **1. Install Dependencies**

```bash
pip install langchain langchain-groq langchain-huggingface langchain-community
pip install faiss-cpu sentence-transformers pandas openpyxl python-dotenv
```

### **2. Configure API Key**

Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### **3. Prepare Data**

Download TMDB dataset:
```bash
# Place these files in data/ directory:
# - movies_metadata.csv
# - credits.csv
```

### **4. Run the Notebook**

```bash
jupyter notebook movie_recommender.ipynb
```

### **5. Start Interactive Chat**

```python
# In the notebook, run:
interactive_chat()
```

---

## 📈 Performance Metrics

### **Vector Store Performance**
- **Build Time**: 124.43 seconds (one-time)
- **Load Time**: ~2 seconds (subsequent runs)
- **Search Time**: <100ms per query

### **Agent Response Times**
- **Simple Query**: 1-3 seconds
- **Tool Execution**: 2-5 seconds
- **Complex Multi-Step**: 5-10 seconds

### **Memory Efficiency**
- **Context Window**: 4 messages (~1200 tokens)
- **Token Savings**: ~70% vs full history
- **Rate Limit Errors**: 0 (after optimization)

---

## 🎓 Learning Outcomes

This mid-project successfully demonstrates:

1. **End-to-End RAG System**: From raw CSV to production-ready semantic search
2. **Agent Design Patterns**: ReAct architecture with real-world tool integration
3. **Production Considerations**: Error handling, logging, retry logic, user validation
4. **Memory Optimization**: Token-efficient conversation management
5. **Data Engineering**: ETL pipeline for movie metadata + credits
6. **User Experience**: Interactive validation, fuzzy matching, helpful error messages
7. **State Management**: Excel persistence, JSON backups, session recovery

---

## 🔮 Future Enhancements

### **Planned Features**
- [ ] Filter watchlist by genre and rating range
- [ ] Export recommendations to PDF report
- [ ] Multi-user support with separate watchlists
- [ ] Integration with streaming service APIs
- [ ] Sentiment analysis on user reviews
- [ ] Movie trailer embedding and playback
- [ ] Social features (share watchlists)
- [ ] GraphRAG for actor/director relationship queries

---

# 🚀 Task 1: Structured Information Extractor

## 📋 Objective

Develop a reliable information extraction engine that transforms unstructured job applications, resumes, or self-introductions into strict, validated JSON formats without hallucinating missing information.

## 💡 Implementation Details

### 1. Schema Definition

Created a `Candidate` Pydantic `BaseModel` enforcing a structured schema containing:

* `Candidate_name`
* `Years_of_experience`
* `Current_role`
* `Skills`
* `Highest_Education`

Pydantic ensures that the extracted information follows the expected data types and structure.

### 2. Structured Parsing

Integrated LangChain's `PydanticOutputParser` to inject the required JSON schema and formatting instructions into the LLM prompt.

This ensures that the model returns data that can be validated against the predefined Pydantic schema.

### 3. Strict Guardrails

The extraction prompt explicitly instructs the model to:

* Never fabricate missing information
* Return `null` when a parameter is unavailable
* Return an empty array `[]` when no skills are available
* Extract only information supported by the provided text

### 4. LCEL Chain Assembly

The extraction pipeline was implemented using **LangChain Expression Language (LCEL)**:

```text
PromptTemplate
      ↓
ChatGroq
      ↓
PydanticOutputParser
```

This creates a clean and modular extraction workflow.

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

Build an AI Agent capable of dynamic goal execution.

The agent interprets natural-language queries, autonomously selects the appropriate tool, extracts the required parameters, interacts with internal databases and APIs, and maintains the conversation flow statefully.

## 🧠 Agent Architecture

The agent was implemented using `LangGraph StateGraph`, with conditional routing and custom tool integrations.

## 🧰 Available Tools

### 📊 Analytics Tool — `analytics_tool`

Computes statistical metrics over numerical arrays:

* Average
* Maximum
* Minimum
* Count

Example:

```text
Average: 25.4
Maximum: 50
Minimum: 10
Count: 8
```

### 🌍 Location Information Tool — `location_tool`

Provides geographic and timezone information for cities and landmarks.

It integrates:

* geopy
* Nominatim API
* timezonefinder
* pytz

The tool can retrieve:

* Exact location information
* Country
* Timezone
* Current local time

### 📅 Schedule Management Tool — `scheduler_tool`

Connects to a local SQLite database:

```text
schedule.db
```

The scheduler supports:

* Event creation
* Event deletion
* Schedule management
* Automatic conflict detection

Before inserting a new event, the tool checks whether an existing event conflicts with the requested time.

## 🔄 Agentic Workflow Architecture

The LangGraph workflow consists of three main components.

### 1. Agent Node — `call_model`

The agent evaluates:

* Conversation history
* System instructions
* Available tools
* User intent

It then decides whether to:

* Call a tool
* Return a final response

### 2. Tool Node — `ToolNode`

`ToolNode` executes the tool calls generated by the LLM.

The available Python tools are executed natively through LangGraph's tool-calling mechanism.

### 3. Conditional Edge — `should_continue`

The conditional routing determines whether the workflow should:

* Continue to the tools when tool calls are present
* Terminate at `END` when the agent has generated the final response

## 📐 Workflow Diagram

```text
                 +-----------+
                 |   START   |
                 +-----+-----+
                       |
                       v
                +--------------+
                |  agent Node  |
                | call_model() |
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
               | Tool Output
               |
               +------------------+
                                  |
                                  v
                           +--------------+
                           |  agent Node  |
                           +--------------+
```

This creates an iterative agentic loop:

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

The goal of this project is to fine-tune a pre-trained open-source language model to specialize in answering technical support questions, transforming a general-purpose model into a highly focused, domain-specific assistant for medical conversations.

## 💡 Implementation Details

### 1. Model Initialization

Loaded the pre-trained open-source model:

```text
mistralai/Mistral-7B-Instruct-v0.3
```

To drastically reduce memory usage, the model was loaded using **4-bit quantization** through `BitsAndBytesConfig`.

### 2. Dataset Preparation

Extracted and prepared the following dataset:

```text
FreedomIntelligence/medical-o1-reasoning-SFT
```

The dataset contains structured medical Q&A pairs.

The data was mapped and formatted into Mistral's instruction style:

```text
<s>[INST] {question} [/INST] {answer} </s>
```

This format prepares the dataset for instruction fine-tuning.

### 3. Parameter-Efficient Fine-Tuning (PEFT)

Configured and applied **LoRA (Low-Rank Adaptation)**.

| Parameter | Value |
|-----------|-------|
| Rank (`r`) | 16 |
| Alpha (`lora_alpha`) | 32 |
| Dropout | 0.05 |
| Trainable Parameters | ~1.1% |

The adapters target attention projection layers such as:

* `q_proj`
* `k_proj`
* `v_proj`
* Other attention projection layers

This significantly reduces the number of parameters that need to be trained.

### 4. Training and Persistence

The model was trained for **2 epochs**.

A larger effective batch size was simulated using **gradient accumulation**.

The resulting:

* Fine-tuned adapter weights
* Tokenizer configuration

were successfully saved locally.

### 5. Evaluation and Integration

Generated and compared responses before and after fine-tuning to evaluate the model's adaptation to the medical domain.

The specialized model was then integrated into a LangChain workflow using:

* `HuggingFacePipeline`
* `PromptTemplate`
* `StrOutputParser`

## 💻 Expected Output

```text
================================================================================
COMPARISON: BEFORE vs AFTER FINE-TUNING
================================================================================

📝 Question:

If suddenly when I walk my stomach started to hurt me,
what do you think it is and what is your suggestion?

🔴 BEFORE FINE-TUNING (General Mistral):

I'm not a doctor, but I can suggest some common causes
of stomach pain...

(Proceeds with generic possibilities such as indigestion
or food poisoning.)

🟢 AFTER FINE-TUNING (Medical-Specialized Mistral):

If you experience stomach pain while walking, it could be
due to a condition called intermittent claudication.
This condition is often associated with peripheral artery
disease...

To address this issue, it's important to manage your
overall cardiovascular health.

================================================================================
```

> **Note:** The example above represents the observed model behavior during evaluation and should not be interpreted as medical advice or as a clinically validated diagnosis.

---

# 📚 Task 4: Simple RAG System

## 📋 Objective

Use **RAG (Retrieval-Augmented Generation)** to answer questions based on PDF documents serving as a knowledge base.

The goal is to build a robust system consisting of a retriever and generator that strictly grounds its answers in the provided context and refuses to hallucinate.

## 💡 Implementation Details

### 1. Document Loading and Splitting

Loaded **7 PDFs** containing course material on Parallel Computing from a local directory.

The documents were split using LangChain's `RecursiveCharacterTextSplitter`.

Configuration:

* Chunk Size: `1000` characters
* Chunk Overlap: `150` characters
* Result: `56` semantic chunks

This structure optimizes the documents for vector retrieval.

### 2. Vector Database & Embedding

Initialized the following lightweight embedding model:

```text
all-MiniLM-L6-v2
```

The 56 chunks were transformed into numerical vectors and stored in a **FAISS** vector database.

The implementation uses a **Flat Index with L2 distance** for brute-force similarity search, which is suitable for this small dataset.

### 3. Action 1: Retriever Testing

Before passing data to the LLM, a dedicated retrieval flow was built to:

* Search the FAISS database
* Retrieve the top 3 most relevant chunks
* Verify that semantic search isolates the relevant context

### 4. Action 2: Generation with Strict Guardrails

Integrated Groq using:

```text
openai/gpt-oss-120b
```

as the generator LLM.

A restrictive `PromptTemplate` was engineered to reduce hallucination.

The prompt explicitly forces the model to return a fallback response when the answer is missing from the retrieved context:

```text
Ana ma3rafsh el ma3looma de, msh mawgooda fe el PDFs.
```

### 5. Final RAG Chain

Combined the retriever and the LLM using:

* `create_retrieval_chain`
* `create_stuff_documents_chain`

This creates an end-to-end question-answering pipeline.

## 💻 Expected Output

```text
--- Running Full RAG Pipeline ---

Question:
What is the difference between shared memory and distributed memory in parallel computing?

Answer:

Shared memory
- One global memory space that all processors can address directly.
- Programming is easier because data are accessed with ordinary pointers.
- Communication happens through memory reads and writes.
- Fast data sharing through direct memory access.
- Drawbacks include limited scalability, cache-coherency overhead,
  synchronization requirements, and higher hardware complexity.

Distributed memory
- Each processor has its own private local memory.
- Processors exchange data through a network.
- Memory capacity scales with the number of processors.
- Local memory access is fast and avoids cache-coherency issues.
- The programmer must explicitly manage communication and data distribution.

Key difference:

Shared memory provides a single globally accessible address space with
simpler programming but limited scalability, whereas distributed memory
gives each processor its own memory, providing better scalability at the
cost of more complex communication management.
```

Example of an unsupported question:

```text
Question:
How to bake a chocolate cake?

Answer:
I don't know, this information is not in the context.
```

---

# 🧠 Task 6: Advanced Conversational Memory Management

## 📋 Objective

Build a robust, stateful memory system for conversational agents to maintain context over long interactions.

This implementation integrates:

* Rolling summaries
* Conversation history
* Persistent JSON storage

to manage conversation state effectively.

## 💡 Implementation Details

### 1. Rolling Summarization

Implemented a dynamic summary engine:

```python
_summarize_conversation()
```

The function condenses older messages into a compact summary while preserving:

* Essential information
* Key topics discussed
* Important facts
* Decisions made

### 2. Object-Oriented State Management (OOP)

Encapsulated the entire workflow within a modular:

```python
ConversationalAgent
```

class.

The agent:

* Automatically creates a context prompt
* Combines a system message, rolling summary, and user input
* Maintains a complete `conversation_history`
* Stores timestamps for each interaction

### 3. Persistent Storage (JSON)

Added serialization methods:

```python
save_conversation()
load_conversation()
```

These allow the conversation history and summary to be saved locally.

Default file:

```text
conversation_log.json
```

This allows sessions to be paused and loaded later.

## 💻 Expected Output

### JSON Save Format

```json
{
  "conversation_history": [
    {
      "user": "Hi! My name is Bavly and I'm an AI engineer working on AI projects.",
      "assistant": "Hello Bavly! 👋 Nice to meet you. It's great to connect with an AI engineer. What kind of AI projects are you working on right now? Anything exciting you'd like to share or discuss?",
      "timestamp": "2026-09-14T13:54:19.260451"
    },
    {
      "user": "I'm 21 years old.",
      "assistant": "Thanks for letting me know! 😊 Is there anything specific you'd like to chat about or any project you're working on that I can help with?",
      "timestamp": "2026-09-14T13:56:14.619902"
    }
  ],
  "summary": "**Summary of Conversation**\n\n- **Participants**\n  - *User (Bavly)*: AI engineer, 21 years old, working on a chatbot with memory management.\n  - *Assistant*: Provides guidance and acknowledges user information."
}
```

---

# ✈️ Task 7: Multi-Agent Travel Planning System

## 📋 Objective

Build an intelligent, two-phase travel planning system that combines **conversational AI** with **multi-agent collaboration** to collect user requirements and generate personalized travel plans.

The system demonstrates:
- Interactive requirement gathering with memory
- Sequential multi-agent pipeline architecture
- Structured data flow between specialized agents
- Production-ready error handling

## 🎯 What I Built

### **Two-Phase Architecture**

#### **Phase 1: Interactive Intake Agent**
A conversational agent that collects travel requirements through natural dialogue:
- **Memory**: `ConversationBufferWindowMemory` (k=4) for context retention
- **Validation**: Ensures all 4 required fields are collected
- **Output**: Validated JSON with destination, budget, interests, and time

#### **Phase 2: Sequential Multi-Agent Pipeline**
Four specialized agents working in sequence:

1. **Destination Agent**: Analyzes user preferences and recommends specific places and activities
2. **Budget Agent**: Creates detailed cost breakdown across all expense categories
3. **Itinerary Agent**: Generates day-by-day schedule with timing and locations
4. **Recommendation Agent**: Synthesizes all information into a beautiful markdown travel report

---

## 🏗️ System Architecture

### **Data Flow Diagram**

```text
┌─────────────────────────────────────────────────────────┐
│             PHASE 1: INTAKE AGENT                       │
│                                                          │
│   User Input → Memory (k=4) → LLM → JSON Validation    │
│                                           ↓              │
│                          Requirements JSON               │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│          PHASE 2: MULTI-AGENT PIPELINE                  │
│                                                          │
│  Requirements JSON                                       │
│         ↓                                                │
│  Agent 1 (Destination) → Places & Activities JSON       │
│         ↓                                                │
│  Agent 2 (Budget) → Cost Breakdown JSON                 │
│         ↓                                                │
│  Agent 3 (Itinerary) → Day-by-Day Schedule JSON        │
│         ↓                                                │
│  Agent 4 (Recommendation) → Markdown Report             │
└─────────────────────────────────────────────────────────┘
```

### **Agent Communication Pattern**

```text
Intake Agent (Conversational)
    ↓ [JSON: destination, budget, interests, time]
    
Destination Agent (Analytical)
    ↓ [JSON: places[], activities[], highlights]
    
Budget Agent (Financial)
    ↓ [JSON: accommodation, food, transport, total, status]
    
Itinerary Agent (Planning)
    ↓ [JSON: daily_schedule[], duration]
    
Recommendation Agent (Synthesis)
    ↓ [Markdown: Complete travel guide]
```

---

## 💡 Implementation Highlights

### **1. Conversational Intake with Memory**

```python
class ConversationBufferWindowMemory:
    """Keeps last 4 messages for context"""
    k = 4  # 2 conversation pairs
```

**Features:**
- Natural dialogue flow
- Friendly, enthusiastic tone
- Tracks collected vs. missing information
- Outputs JSON only when all 4 fields present

**Sample Interaction:**
```text
🤖: Where would you like to go?
👤: Egypt
🤖: Great choice! What's your budget?
👤: $2000 for two people
🤖: Perfect! What are your interests?
👤: Beaches
🤖: Lastly, how many days do you have?
👤: 5 days

✅ {
  "destination": "Egypt",
  "budget": "$2000 for two persons",
  "interests": "beaches",
  "time": "5 days"
}
```

### **2. JsonOutputParser for Groq Compatibility**

**Challenge:** Groq's `openai/gpt-oss-120b` model doesn't support `with_structured_output()` (requires tool calling)

**Solution:** Replaced Pydantic-based parsing with `JsonOutputParser`

```python
# ❌ Doesn't work with Groq
structured_llm = llm.with_structured_output(Model)

# ✅ Works universally
json_parser = JsonOutputParser()
chain = prompt | llm | json_parser
```

### **3. Type-Safe Data Conversion**

**Problem:** LLMs sometimes return lists of dicts instead of strings

```json
❌ ["{"name": "Pyramid"}", "{"name": "Museum"}"]
✅ ["Pyramid", "Museum"]
```

**Solution:** Helper function handles both formats

```python
def convert_to_string_list(data):
    """Extracts strings from dicts or returns as-is"""
    result = []
    for item in data:
        if isinstance(item, dict):
            # Extract from 'name', 'place', 'activity', etc.
            result.append(extract_relevant_value(item))
        else:
            result.append(str(item))
    return result
```

### **4. Structured Prompts with Format Instructions**

Each agent receives explicit JSON schema examples:

```python
prompt = f"""
Return ONLY valid JSON in this format:
{{
  "places": ["Place 1", "Place 2"],
  "activities": ["Activity 1", "Activity 2"],
  "highlights": "Text here"
}}
"""
```

### **5. Safe Dictionary Access**

**Before (causes AttributeError):**
```python
places = destination_output.places  # Fails - dict, not object
```

**After (production-safe):**
```python
places = destination_output.get('places', [])  # Returns [] if missing
```

---

## 🛠️ Technical Challenges & Solutions

### **Challenge 1: Tool Calling Incompatibility**

**Error:**
```python
BadRequestError: Tool choice is required, but model did not call a tool
```

**Root Cause:**  
`with_structured_output()` uses function calling internally, which Groq doesn't support

**Solution:**  
Switched to `JsonOutputParser` which works with any JSON-capable LLM

**Impact:** ✅ Universal compatibility across LLM providers

---

### **Challenge 2: Mixed Data Types from LLM**

**Error:**
```python
TypeError: sequence item 0: expected str instance, dict found
```

**Root Cause:**  
LLM returned `[{"place": "Cairo"}, {"place": "Alexandria"}]` instead of `["Cairo", "Alexandria"]`

**Solution:**  
Created `convert_to_string_list()` helper function

**Impact:** ✅ Robust handling of variable LLM outputs

---

### **Challenge 3: Dictionary vs Object Access**

**Error:**
```python
AttributeError: 'dict' object has no attribute 'places'
```

**Root Cause:**  
`JsonOutputParser` returns Python dicts, not Pydantic objects

**Solution:**  
Replaced all `.attribute` access with `.get('key', default)`

**Impact:** ✅ No crashes from missing keys, graceful degradation

---

## 📊 System Specifications

| Component | Technology |
|-----------|------------|
| **LLM Provider** | Groq |
| **Model** | `openai/gpt-oss-120b` |
| **Framework** | LangChain (LCEL) |
| **Memory** | ConversationBufferWindowMemory (k=4) |
| **Output Parsing** | JsonOutputParser |
| **Agent Pattern** | Sequential Pipeline (not LangGraph) |
| **Data Flow** | JSON → JSON → JSON → Markdown |
| **Error Handling** | `.get()` methods, type conversion |

---

## 💻 Sample Output

### **Phase 1: Requirements Collection**

```json
{
  "destination": "Egypt",
  "budget": "$2000 USD for two persons",
  "interests": "beaches",
  "time": "5 days"
}
```

### **Phase 2: Agent Pipeline**

**Agent 1 Output (Destination):**
```json
{
  "places": [
    "Hurghada Beach",
    "Sharm El Sheikh",
    "Marsa Alam",
    "Alexandria Corniche",
    "Ras Mohammed National Park",
    "Giftun Island"
  ],
  "activities": [
    "Snorkeling in Red Sea",
    "Beach relaxation",
    "Diving excursions",
    "Boat tours",
    "Water sports",
    "Sunset viewing"
  ],
  "highlights": "Egypt's Red Sea coast offers pristine beaches..."
}
```

**Agent 2 Output (Budget):**
```json
{
  "accommodation": "$60 per night, $300 total",
  "food": "$30 per day, $150 total",
  "transport": "$200 (flights + local)",
  "activities": "$100 (snorkeling, tours)",
  "miscellaneous": "$50 (tips, souvenirs)",
  "total": "$800",
  "budget_status": "Well within budget - $1200 remaining"
}
```

**Agent 3 Output (Itinerary):**
```json
{
  "daily_schedule": [
    "Day 1: Arrive Hurghada, check-in, evening beach walk",
    "Day 2: Morning snorkeling, afternoon at Giftun Island",
    "Day 3: Day trip to Ras Mohammed National Park",
    "Day 4: Beach relaxation, water sports, sunset cruise",
    "Day 5: Morning dive, afternoon departure"
  ],
  "duration": "5 days"
}
```

**Agent 4 Output (Final Report):**
```markdown
# 🌊 Your Egypt Beach Paradise - 5-Day Escape

## ✨ Destination Overview

Egypt's Red Sea coast offers world-class beaches, vibrant coral reefs, 
and year-round sunshine. Perfect for beach lovers seeking relaxation 
and underwater adventures.

## 📅 Your Day-by-Day Itinerary

### Day 1: Arrival & Beach Welcome
- **Morning**: Arrive in Hurghada
- **Afternoon**: Hotel check-in, settle in
- **Evening**: Sunset beach walk along the corniche

### Day 2: Underwater Wonderland
- **Morning**: Snorkeling trip (Red Sea coral reefs)
- **Afternoon**: Boat excursion to Giftun Island
- **Evening**: Fresh seafood dinner by the beach

[... complete 5-day schedule ...]

## 💰 Budget Breakdown

| Category | Cost |
|----------|------|
| Accommodation | $300 |
| Food | $150 |
| Transport | $200 |
| Activities | $100 |
| Miscellaneous | $50 |
| **Total** | **$800** |

✅ **Budget Status**: Well within your $2000 budget! 
You have $1200 remaining for upgrades or extensions.

## 🎒 What to Pack

- Sunscreen (SPF 50+)
- Swimwear and beach towel
- Snorkeling gear (or rent locally)
- Light, breathable clothing
- Hat and sunglasses
- Underwater camera

## 💡 Travel Tips

1. **Best Time**: October-April for cooler weather
2. **Currency**: Egyptian Pound (cash recommended)
3. **Snorkeling**: Book through hotel for best rates
4. **Safety**: Red Sea is generally safe for swimming

## 🌟 Final Thoughts

Your Egyptian beach getaway combines relaxation with adventure. 
The Red Sea's crystal-clear waters and vibrant marine life will 
create memories to last a lifetime. Safe travels! 🏖️✨
```

---

## 🎓 Key Concepts Demonstrated

### **Multi-Agent Collaboration**
- ✅ Sequential agent pipeline (not parallel)
- ✅ Structured data passing between agents
- ✅ Specialized agent roles (analysis, budgeting, planning, synthesis)
- ✅ Clean separation of concerns

### **Conversational AI**
- ✅ Stateful conversation with memory
- ✅ Context retention (k=4 window)
- ✅ Natural language to JSON extraction
- ✅ Interactive requirement gathering

### **Production Engineering**
- ✅ Error-tolerant dictionary access
- ✅ Type conversion for mixed LLM outputs
- ✅ API compatibility handling (Groq-specific)
- ✅ Graceful degradation (missing keys return defaults)

### **LangChain Patterns**
- ✅ LCEL chain composition
- ✅ JsonOutputParser for universal compatibility
- ✅ PromptTemplate with format instructions
- ✅ Memory integration

---

## 📁 Project Structure

```text
Task 7/
│
├── multi_agent_travel_planner_final.ipynb    # Complete implementation
│
├── README.md                                  # This documentation
│
└── .env                                       # GROQ_API_KEY
```

---

## 🚀 How to Run

### **1. Install Dependencies**

```bash
pip install langchain langchain-groq langchain-core python-dotenv
```

### **2. Configure API Key**

Create `.env`:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### **3. Run the Notebook**

```bash
jupyter notebook multi_agent_travel_planner_final.ipynb
```

### **4. Execute Cells Sequentially**

Run all cells from top to bottom. The final cell starts the interactive chat:

```python
if __name__ == "__main__":
    result = main()
```

---

## 🎯 Learning Outcomes

This task successfully demonstrates:

1. **Two-Phase System Design**: Separating intake from processing
2. **Sequential Agent Orchestration**: Passing structured data between agents
3. **API Compatibility Handling**: Groq-specific workarounds
4. **Production Error Handling**: Type safety, missing key handling
5. **Conversational Memory**: Context retention without token bloat
6. **Structured Output Parsing**: JSON schemas with format instructions
7. **End-to-End Pipeline**: From natural language to formatted report

---

## 🔮 Potential Enhancements

- [ ] Add parallel agent execution for speed (using asyncio)
- [ ] Integrate external APIs (flights, hotels, weather)
- [ ] Add user feedback loop (refine recommendations)
- [ ] Implement conversation history persistence
- [ ] Add image generation for destinations
- [ ] Export reports to PDF format
- [ ] Multi-language support for international travelers

---

# 🎫 Task 8: Customer Support Ticket System

## 📋 Objective

Build an AI-powered customer support ticket routing system that automatically analyzes incoming support queries, classifies the problem, determines its priority, detects multiple issues, and creates persistent support tickets.

The system combines **LangGraph**, **FastAPI**, **Groq LLM**, and **SQLite** to create an end-to-end ticket processing workflow.

## 🎯 What I Built

The system provides the following capabilities:

* **Intelligent Problem Classification** — Categorizes support queries into:

  * Technical
  * Billing
  * Account
  * General
  * NONE for unsupported or off-topic requests
* **Priority Assignment** — Assigns:

  * HIGH
  * MEDIUM
  * LOW
* **Multi-Issue Detection** — Identifies multiple problems in a single customer query and creates separate tickets for each issue.
* **UUID-Based Tickets** — Generates a unique identifier for every ticket.
* **Email-Based Retrieval** — Retrieves all tickets associated with a customer's email.
* **Persistent Storage** — Stores ticket information in a SQLite database.
* **REST API** — Exposes the ticket system through FastAPI endpoints.

## 🏗️ System Architecture

The core workflow is implemented using **LangGraph**:

```text
Customer Query
      ↓
┌──────────────────────┐
│ Classify Problem     │
└──────────┬───────────┘
           ↓
     Is problem NONE?
       /          \
     Yes           No
      ↓             ↓
     END     Classify Priority
                    ↓
             Create Ticket(s)
                    ↓
              SQLite Database
                    ↓
                   END
```

### LangGraph Workflow

The workflow separates the ticket-processing logic into dedicated nodes:

1. **Problem Classification Node**

   * Analyzes the customer's query.
   * Identifies the support category.
   * Detects whether the query contains multiple issues.

2. **Conditional Routing**

   * Routes unsupported queries directly to the end.
   * Continues valid support requests through the ticket workflow.

3. **Priority Classification Node**

   * Determines the urgency of each identified issue.
   * Assigns HIGH, MEDIUM, or LOW priority.

4. **Ticket Creation Node**

   * Generates UUID-based ticket IDs.
   * Creates individual tickets for each detected problem.
   * Stores the tickets in SQLite.

## 🧠 Problem Categories

| Category      | Examples                                   |
| ------------- | ------------------------------------------ |
| **Technical** | System errors, bugs, outages               |
| **Billing**   | Payment issues, duplicate charges, refunds |
| **Account**   | Login, password, profile problems          |
| **General**   | Feature questions, how-to requests         |
| **NONE**      | Spam, unsupported, or off-topic queries    |

## 🚨 Priority System

| Priority   | Response Time | Examples                                                             |
| ---------- | ------------- | -------------------------------------------------------------------- |
| **HIGH**   | 2 hours       | Complete outage, security breach, critical payment errors, data loss |
| **MEDIUM** | 24 hours      | Partial disruptions, billing inquiries, account access issues        |
| **LOW**    | 48 hours      | General questions, minor UI issues, documentation requests           |

## 🌐 FastAPI REST API

The LangGraph workflow is exposed through a FastAPI server.

### Create Ticket

```text
POST /api/ticket
```

Example request:

```json
{
  "query": "I can't access my account and was charged twice",
  "name": "John Doe",
  "email": "john@example.com"
}
```

A multi-issue query can produce multiple tickets:

```json
{
  "success": true,
  "message": "Successfully created 2 ticket(s)",
  "tickets": [
    {
      "ticket_id": "uuid-1",
      "problem_type": "Account",
      "priority": "HIGH",
      "estimated_response_time": "2 hours"
    },
    {
      "ticket_id": "uuid-2",
      "problem_type": "Billing",
      "priority": "MEDIUM",
      "estimated_response_time": "24 hours"
    }
  ]
}
```

### Available Endpoints

| Method   | Endpoint                  | Purpose                            |
| -------- | ------------------------- | ---------------------------------- |
| **POST** | `/api/ticket`             | Create one or more support tickets |
| **GET**  | `/api/tickets/{email}`    | Retrieve tickets by customer email |
| **GET**  | `/api/tickets`            | Retrieve all tickets               |
| **GET**  | `/api/ticket/{ticket_id}` | Retrieve a ticket by ID            |
| **GET**  | `/health`                 | Check API health                   |

## 🗄️ Database Design

Ticket data is persisted using SQLite.

```sql
CREATE TABLE tickets (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    query TEXT NOT NULL,
    problem_type TEXT NOT NULL,
    priority TEXT NOT NULL,
    estimated_response_time TEXT,
    created_at TIMESTAMP NOT NULL
);
```

The database stores the customer's information, original query, classification result, priority, expected response time, and creation timestamp.

## 🧪 Example Scenarios

### Single Issue

```text
Query:
"I can't login to my account"

Result:
1 ticket → Account → HIGH
```

### Multiple Issues

```text
Query:
"The system is down and I was charged twice!"

Result:
2 tickets

Technical → HIGH
Billing   → MEDIUM
```

### Unsupported Query

```text
Query:
"Buy cheap watches now!"

Result:
No support ticket created.
The system identifies the query as unsupported.
```

## 🛠️ Technical Challenges & Solutions

### Challenge 1: Multi-Issue Queries

**Problem:** A customer can mention multiple independent problems in a single message.

**Solution:** The classification workflow identifies separate issues and creates an individual ticket for each problem, allowing them to be routed and prioritized independently.

### Challenge 2: Conditional Workflow Routing

**Problem:** Unsupported queries should not continue through the ticket creation pipeline.

**Solution:** LangGraph conditional routing checks the classification result and terminates the workflow when the problem type is `NONE`.

### Challenge 3: Persistent Ticket Management

**Problem:** Tickets need to remain available after the application restarts.

**Solution:** Implemented SQLite-based persistence with dedicated database operations for creating and retrieving tickets.

### Challenge 4: API Integration

**Problem:** The AI workflow needs to be accessible to external clients.

**Solution:** Wrapped the LangGraph workflow with FastAPI REST endpoints and added Swagger/OpenAPI documentation for interactive testing.

## 📊 System Specifications

| Component                  | Technology            |
| -------------------------- | --------------------- |
| **LLM Provider**           | Groq                  |
| **Model**                  | `openai/gpt-oss-120b` |
| **Agent Framework**        | LangGraph             |
| **API Framework**          | FastAPI               |
| **Database**               | SQLite                |
| **Data Validation**        | Pydantic              |
| **Ticket IDs**             | UUID                  |
| **Environment Management** | python-dotenv         |
| **Language**               | Python                |

## 🎓 Key Concepts Demonstrated

### Agentic AI

* ✅ LangGraph workflow orchestration
* ✅ Conditional routing
* ✅ LLM-based classification
* ✅ Multi-step AI processing

### Backend Engineering

* ✅ FastAPI REST API development
* ✅ Request/response validation
* ✅ SQLite database integration
* ✅ Persistent CRUD operations
* ✅ API health monitoring

### AI-Powered Automation

* ✅ Automatic problem classification
* ✅ Priority assignment
* ✅ Multi-issue detection
* ✅ Automated ticket generation
* ✅ Email-based ticket retrieval

## 📁 Project Structure

```text
Task 8 - Customer Support Ticket System/
│
├── agent/
│   ├── __init__.py
│   ├── nodes.py          # Classification and ticket creation nodes
│   ├── edges.py          # Conditional routing logic
│   └── agent.py          # LangGraph workflow
│
├── database.py            # SQLite schema and operations
├── main.py                # FastAPI server and endpoints
├── test_api.py            # API testing
├── requirements.txt       # Dependencies
├── .env.example           # Environment configuration
└── README.md              # Task documentation
```

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Start the FastAPI server:

```bash
python main.py
```

The API can then be tested through the FastAPI Swagger UI:

```text
http://localhost:8000/docs
```

## 🎯 Learning Outcomes

This task demonstrates:

1. **LangGraph Workflow Design** — Building a structured AI workflow with nodes and conditional edges.
2. **LLM-Based Classification** — Using an LLM to understand and categorize natural-language support requests.
3. **Multi-Issue Processing** — Converting one customer message into multiple independently managed tickets.
4. **Backend API Development** — Exposing an AI workflow through FastAPI.
5. **Database Integration** — Persisting AI-generated results using SQLite.
6. **End-to-End AI Engineering** — Connecting an LLM, workflow engine, API layer, and database into a complete application.

---


# 🗂️ Project Structure

```text
.
├── Task 1/
│   ├── task1.ipynb
│   └── ...                       # Additional Task 1 assets
│
├── Task 2 - langgraph/
│   ├── agent/
│   │   └── ...                   # Agent configuration and nodes
│   │
│   ├── database/
│   │   └── schedule.db           # SQLite scheduling database
│   │
│   ├── tools/
│   │   ├── analytics_tool
│   │   ├── location_tool
│   │   └── scheduler_tool
│   │
│   └── main.py                   # Main execution script
│
├── Task 3/
│   └── task3.ipynb               # Mistral 7B fine-tuning and LangChain integration
│
├── Task 4 - RAG/
│   ├── pdfs/                     # Parallel computing knowledge base
│   │   └── ...                   # 7 PDF documents
│   ├── faiss_parallel_computing_index/
│   └── task4.ipynb               # RAG pipeline implementation
│
├── Task 6 - Memory/
│   ├── agent_with_memory.ipynb   # Conversational memory implementation
│   └── conversation_log.json     # Saved conversation state
│
├── 🎬 Mid-Project - Movie Recommender/
│   ├── movie_recommender.ipynb   # Full implementation
│   ├── data/
│   │   ├── movies_metadata.csv   # 45K+ movies
│   │   └── credits.csv           # Cast & crew
│   ├── faiss_index/              # Vector store (44K documents)
│   ├── memory/                   # Conversation storage
│   ├── logs/                     # Performance logs
│   └── my_watchlist.xlsx         # User watchlist
│
├── Task 7 - Multi-Agent Travel Planner/
│   ├── multi_agent_travel_planner_final.ipynb   # Sequential agents
│   └── README.md                                 # Task 7 docs
│
│
├── Task 8 - Customer Support Ticket System/
│   ├── agent/
│   │   ├── **init**.py
│   │   ├── nodes.py
│   │   ├── edges.py
│   │   └── agent.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── test_api.py
│   ├── requirements.txt
│   └── .env.example

│
├── .env                          # Environment variables
├── .gitignore
├── README.md
├── requirements.txt
│
├── Task 1 (Output Parser).pdf
├── Task 2 (AI Agent).pdf
├── Task 3 (Fine-Tuning).pdf
├── Task 4 (RAG).pdf
└── Task 7 (Multi-Agent Collaboration).pdf
```

> **Security Note:** Make sure `.env` and any other files containing secrets are included in `.gitignore` and are never committed to the repository.

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

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

---

# ▶️ Running the Projects

## Task 2: Multi-Tool Agent

```bash
cd "Task 2 - langgraph"
python main.py
```

## Task 1, 3, 4, 6, 7, Mid-Project: Jupyter Notebooks

```bash
jupyter notebook
```

Then open the respective `.ipynb` files.

---

# 🎯 Key Concepts Demonstrated

## LLM & Prompt Engineering

* LLM structured output
* Prompt engineering
* Guardrails
* LangChain Output Parsers
* LangChain Expression Language (LCEL)
* Format instructions for JSON schemas

## Agentic AI

* LLM tool calling
* LangGraph `StateGraph`
* Conditional graph routing
* Stateful AI agents
* Multi-tool orchestration
* **Sequential multi-agent pipelines**
* Agentic loops
* Tool execution
* ReAct (Reasoning + Acting) pattern
* **Specialized agent roles**

## Vector Databases & Retrieval (RAG)

* Document parsing and chunking
* Semantic search and embeddings
* FAISS Vector Database integration
* Large-scale indexing (44K+ documents)
* Retrieval-Augmented Generation pipelines
* Anti-hallucination prompting techniques
* Persistent vector stores

## Memory & State Management

* Rolling conversation summaries
* Token-efficient memory windows
* **ConversationBufferWindowMemory (k=4)**
* Object-Oriented Bot Architectures for session state
* JSON persistence for saving and loading conversation histories
* Full conversation backups
* **Context retention across agent calls**

## Data & Backend Integration

* Pydantic schema validation
* **JsonOutputParser for universal LLM compatibility**
* External API integration
* Geolocation and timezone services
* SQLite database integration
* Excel file operations (XLSX)
* Schedule conflict detection
* ETL pipelines for large datasets
* Fuzzy string matching
* Environment and API-key management
* **Type-safe dictionary access patterns**

## LLM Fine-Tuning

* Parameter-Efficient Fine-Tuning (PEFT)
* LoRA
* 4-bit model quantization
* Hugging Face Transformers
* `SFTTrainer`
* Domain-specific assistant training

## Production Engineering

* Error handling and graceful degradation
* Retry logic for file operations
* Performance monitoring and logging
* Interactive user validation
* Rate limit management
* Data type compatibility handling
* **API-specific workarounds (Groq compatibility)**
* **Safe dictionary access with `.get()` methods**
* **Type conversion for mixed LLM outputs**

---

# 🧠 Complete Architecture Summary

The repository demonstrates a complete progression from foundational LLM concepts to production-ready AI systems:

**Foundation** → **Agents** → **Specialization** → **RAG** → **Memory** → **Multi-Agent Collaboration** → **Integration**

### **Progression Timeline**

1. **Task 1**: Structured data extraction
2. **Task 2**: Single agent with multiple tools
3. **Task 3**: Domain-specific model specialization
4. **Task 4**: Knowledge retrieval systems (RAG)
5. **Task 6**: Stateful conversation management
6. **Mid-Project**: Full application (RAG + Agents + Memory)
7. **Task 7**: Multi-agent collaboration & sequential pipelines ✨

---

# 🔐 Security

API credentials and other secrets should always be stored in environment variables rather than hard-coded in source code.

Example:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Add the following to `.gitignore`:

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
```

Never commit actual API keys, tokens, passwords, or other credentials to GitHub.

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
* Large-scale RAG systems (44K+ documents)
* Retrieval-Augmented Generation (RAG) for localized knowledge bases
* Conversational memory and persistent session management
* **Multi-agent collaboration and orchestration** ✨
* **Sequential agent pipelines with structured data flow** ✨
* Production-ready conversational AI assistants
* End-to-end application development

The overall progression demonstrates how modern AI systems can evolve from simple LLM interactions into structured, autonomous, stateful, specialized, **collaborative**, and production-ready AI applications that solve real-world problems through **intelligent agent coordination**.

---

# 📝 License

This project is created for educational purposes as part of AI Engineering coursework.

---

**Last Updated**: September 21, 2026