# 🤖 AI Engineering Tasks & Agentic Systems

Welcome to the **AI Engineering Practice & Frameworks** repository!

This project showcases hands-on implementations of modern **LLM architectures, structured data extraction, autonomous multi-tool AI agents, and domain-specific LLM fine-tuning** using **LangChain, LangGraph, Pydantic, Hugging Face, PEFT, and Groq**.

---

## 📌 Repository Overview

This repository serves as a showcase of practical AI engineering solutions designed to solve real-world automation and intelligent processing challenges.

### Tasks

| Task                                         | Description                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------- |
| **Task 1: Structured Information Extractor** | Enforcing strict schema outputs on unstructured candidate data          |
| **Task 2: Autonomous Multi-Tool AI Agent**   | Building a stateful, tool-calling agent using LangGraph and custom APIs |
| **Task 3: Domain-Specific LLM Fine-Tuning**  | Fine-tuning an open-source LLM for specialized medical customer support |

---

## ⚙️ Core Stack & Tools

| Category                   | Technologies                                       |
| -------------------------- | -------------------------------------------------- |
| **LLM Frameworks**         | LangChain, LangGraph                               |
| **Fine-Tuning & Training** | Hugging Face Transformers, PEFT, TRL, BitsAndBytes |
| **Data Validation**        | Pydantic v2                                        |
| **LLM Engine**             | Groq — `openai/gpt-oss-120b`, Mistral 7B           |
| **Geolocation**            | geopy, timezonefinder, pytz                        |
| **Database**               | SQLite                                             |
| **Environment Management** | python-dotenv                                      |
| **Language**               | Python                                             |

---

# 🚀 Task 1: Structured Information Extractor

## 📋 Objective

Develop a reliable information extraction engine that transforms unstructured **job applications, resumes, or self-introductions** into strict, validated JSON formats without hallucinating missing information.

---

## 💡 Implementation Details

### 1. Schema Definition

Created a `Candidate` Pydantic `BaseModel` enforcing a structured schema containing:

* `Candidate_name`
* `Years_of_experience`
* `Current_role`
* `Skills`
* `Highest_Education`

Pydantic ensures that the extracted information follows the expected data types and structure.

---

### 2. Structured Parsing

Integrated LangChain's `PydanticOutputParser` to inject the required JSON schema and formatting instructions into the LLM prompt.

This ensures that the model returns data that can be validated against the predefined Pydantic schema.

---

### 3. Strict Guardrails

The extraction prompt explicitly instructs the model to:

* Never fabricate missing information.
* Return `null` when a parameter is unavailable.
* Return an empty array `[]` when no skills are available.
* Extract only information supported by the provided text.

---

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

---

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

Build an AI Agent capable of **dynamic goal execution**.

The agent interprets natural-language queries, autonomously selects the appropriate tool, extracts the required parameters, interacts with internal databases/APIs, and maintains the conversation flow statefully.

---

## 🧠 Agent Architecture

The agent was implemented using **LangGraph `StateGraph`**, with conditional routing and custom tool integrations.

---

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

---

### 🌍 Location Information Tool — `location_tool`

Provides geographic and timezone information for cities and landmarks.

It integrates:

* `geopy`
* Nominatim API
* `timezonefinder`
* `pytz`

The tool can retrieve:

* Exact location information
* Country
* Timezone
* Current local time

---

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

---

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

---

### 2. Tool Node — `ToolNode`

`ToolNode` executes the tool calls generated by the LLM.

The available Python tools are executed natively through LangGraph's tool-calling mechanism.

---

### 3. Conditional Edge — `should_continue`

The conditional routing determines whether the workflow should:

* Continue to the tools when tool calls are present.
* Terminate at `END` when the agent has generated the final response.

---

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

This creates an iterative **agentic loop**:

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

The goal of this project is to fine-tune a pre-trained open-source language model to specialize in answering technical support questions, transforming a general-purpose model into a highly focused, domain-specific assistant for **medical conversations**.

---

## 💡 Implementation Details

### 1. Model Initialization

Loaded the pre-trained open-source model:

```text
mistralai/Mistral-7B-Instruct-v0.3
```

To drastically reduce memory usage, the model was loaded using **4-bit quantization** through `BitsAndBytesConfig`.

---

### 2. Dataset Preparation

Extracted and prepared the:

```text
FreedomIntelligence/medical-o1-reasoning-SFT
```

dataset, which contains structured medical Q&A pairs.

The data was mapped and formatted into Mistral's instruction style:

```text
<s>[INST] {question} [/INST] {answer} </s>
```

This format prepares the dataset for instruction fine-tuning.

---

### 3. Parameter-Efficient Fine-Tuning (PEFT)

Configured and applied **LoRA (Low-Rank Adaptation)**.

The LoRA configuration used:

| Parameter            | Value |
| -------------------- | ----: |
| Rank (`r`)           |    16 |
| Alpha (`lora_alpha`) |    32 |
| Dropout              |  0.05 |
| Trainable Parameters | ~1.1% |

The adapters target attention projection layers such as:

```text
q_proj
k_proj
v_proj
...
```

This significantly reduces the number of parameters that need to be trained.

---

### 4. Training and Persistence

The model was trained for:

```text
2 epochs
```

A larger effective batch size was simulated using **gradient accumulation**.

The resulting:

* Fine-tuned adapter weights
* Tokenizer configuration

were successfully saved locally.

---

### 5. Evaluation and Integration

Generated and compared responses **before and after fine-tuning** to evaluate the model's adaptation to the medical domain.

The specialized model was then integrated into a LangChain workflow using:

* `HuggingFacePipeline`
* `PromptTemplate`
* `StrOutputParser`

---

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
├── .env                          # Environment variables
├── .gitignore
├── README.md
├── requirements.txt
│
├── Task 1 (Output Parser).pdf
├── Task 2 (AI Agent).pdf
└── Task 3 (Fine-Tuning).pdf
```

> **Security Note:** Make sure `.env` and any other files containing secrets are included in `.gitignore` and are never committed to the repository.

---

# ⚙️ Setup & Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

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

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace:

```text
your_groq_api_key_here
```

with your actual Groq API key.

---

# ▶️ Running the Project

After installing the dependencies and configuring the environment variables, run **Task 2** from its directory:

```bash
cd "Task 2 - langgraph"
python main.py
```

---

## 📓 Running Task 1 & Task 3

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
Task 1/task1.ipynb
Task 3/task3.ipynb
```

---

# 🎯 Key Concepts Demonstrated

This repository demonstrates practical experience with:

### LLM & Prompt Engineering

* LLM structured output
* Prompt engineering
* LangChain Output Parsers
* LangChain Expression Language (LCEL)
* LLM tool calling

### Agentic AI

* LangGraph `StateGraph`
* Conditional graph routing
* Stateful AI agents
* Multi-tool orchestration
* Agentic loops
* Tool execution

### Data & Backend Integration

* Pydantic schema validation
* External API integration
* Geolocation and timezone services
* SQLite database integration
* Schedule conflict detection
* Environment and API-key management

### LLM Fine-Tuning

* Parameter-Efficient Fine-Tuning (PEFT)
* LoRA
* 4-bit model quantization
* Hugging Face Transformers
* SFTTrainer
* Domain-specific assistant training

---

# 🧠 Architecture Summary

The repository progresses from **structured LLM extraction**, to **autonomous agentic workflows**, and finally to **domain-specific model fine-tuning**.

---

## Task 1 — Structured Information Extraction

```text
┌─────────────────────────────────────────┐
│              Task 1                     │
│      Structured Information Extraction  │
│                                         │
│  Unstructured Text                      │
│        ↓                                │
│  PromptTemplate                         │
│        ↓                                │
│  ChatGroq                               │
│        ↓                                │
│  PydanticOutputParser                   │
│        ↓                                │
│  Validated Structured Data              │
└─────────────────────────────────────────┘
```

---

## Task 2 — Autonomous AI Agent

```text
┌─────────────────────────────────────────┐
│              Task 2                     │
│       Autonomous AI Agent               │
│                                         │
│  User Request                           │
│       ↓                                 │
│  LangGraph Agent                        │
│       ↓                                 │
│  Tool Selection                         │
│       ↓                                 │
│  ┌──────────┬───────────┬───────────┐   │
│  │ Analytics│ Location  │ Scheduler │   │
│  └──────────┴───────────┴───────────┘   │
│       ↓                                 │
│  Tool Results                           │
│       ↓                                 │
│  Agent Re-evaluation                    │
│       ↓                                 │
│  Final Response                         │
└─────────────────────────────────────────┘
```

---

## Task 3 — Domain-Specific LLM Fine-Tuning

```text
┌─────────────────────────────────────────┐
│              Task 3                     │
│   Domain-Specific LLM Fine-Tuning       │
│                                         │
│  Pre-trained Base Model (Mistral 7B)    │
│       ↓                                 │
│  Medical Q&A Dataset Processing         │
│       ↓                                 │
│  Apply LoRA Adapters (PEFT)             │
│       ↓                                 │
│  Train via SFTTrainer                   │
│       ↓                                 │
│  LangChain Integration & Output         │
└─────────────────────────────────────────┘
```

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
```

**Never commit actual API keys, tokens, passwords, or other credentials to GitHub.**

---

# 👨‍💻 Author

**Bavly Waleed**

> AI Engineer | Machine Learning | Computer Vision | Agentic AI

---

# ⭐ Project Purpose

This repository demonstrates the practical application of modern **AI engineering concepts**, moving beyond simple LLM prompting toward:

* Structured and validated LLM outputs
* Stateful AI agents
* Tool-using autonomous workflows
* External API integration
* Database-backed agents
* Parameter-efficient fine-tuning
* Domain-specific language models

The overall progression demonstrates how modern AI systems can evolve from **simple LLM interactions into structured, autonomous, and specialized AI applications**.
