# 🤖 AI Engineering Tasks & Agentic Systems

Welcome to the **AI Engineering Practice & Frameworks** repository!

This project showcases hands-on implementations of modern LLM architectures, structured data extraction, autonomous multi-tool AI agents, domain-specific LLM fine-tuning, Retrieval-Augmented Generation (RAG), and conversational memory management using **LangChain, LangGraph, Pydantic, Hugging Face, FAISS, PEFT, and Groq**.

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
├── .env                          # Environment variables
├── .gitignore
├── README.md
├── requirements.txt
│
├── Task 1 (Output Parser).pdf
├── Task 2 (AI Agent).pdf
├── Task 3 (Fine-Tuning).pdf
└── Task 4 (RAG).pdf
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

## Task 1, 3, 4, 6, Mid-Project: Jupyter Notebooks

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

## Agentic AI

* LLM tool calling
* LangGraph `StateGraph`
* Conditional graph routing
* Stateful AI agents
* Multi-tool orchestration
* Agentic loops
* Tool execution
* ReAct (Reasoning + Acting) pattern

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
* Object-Oriented Bot Architectures for session state
* JSON persistence for saving and loading conversation histories
* Full conversation backups

## Data & Backend Integration

* Pydantic schema validation
* External API integration
* Geolocation and timezone services
* SQLite database integration
* Excel file operations (XLSX)
* Schedule conflict detection
* ETL pipelines for large datasets
* Fuzzy string matching
* Environment and API-key management

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

---

# 🧠 Complete Architecture Summary

The repository demonstrates a complete progression from foundational LLM concepts to production-ready AI systems:

**Foundation** → **Agents** → **Specialization** → **RAG** → **Memory** → **Integration**

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
```

Never commit actual API keys, tokens, passwords, or other credentials to GitHub.

---

# 👨‍💻 Author

**Bavly Waleed**

AI Engineer | Machine Learning | Computer Vision | Agentic AI

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
* **Large-scale RAG systems (44K+ documents)**
* Retrieval-Augmented Generation (RAG) for localized knowledge bases
* Conversational memory and persistent session management
* **Production-ready conversational AI assistants**
* **End-to-end application development**

The overall progression demonstrates how modern AI systems can evolve from simple LLM interactions into structured, autonomous, stateful, specialized, and production-ready AI applications that solve real-world problems.

---

# 📝 License

This project is created for educational purposes as part of AI Engineering coursework.

---

**Last Updated**: September 20, 2026