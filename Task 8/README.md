# Customer Support Ticket System

An AI-powered customer support ticket routing system built with **LangGraph**, **FastAPI**, and **Groq LLM**.

## 🎯 Features

- **Intelligent Problem Classification**: Automatically categorizes queries into Technical, Billing, Account, or General issues
- **Priority Assignment**: Assigns HIGH, MEDIUM, or LOW priority based on urgency
- **Multi-Issue Detection**: Creates separate tickets when a query contains multiple problems
- **UUID-based Tickets**: Each ticket gets a unique identifier
- **Email-based Retrieval**: Query all tickets by user email
- **SQLite Database**: Persistent ticket storage

## 📁 Project Structure

```
.
├── agent/
│   ├── __init__.py       # Package initialization
│   ├── nodes.py          # LangGraph nodes (classification, ticket creation)
│   ├── edges.py          # Conditional routing logic
│   └── agent.py          # Workflow orchestration
├── database.py           # SQLite schema and operations
├── main.py               # FastAPI server and endpoints
├── test_api.py           # Automated and interactive testing
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md             # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file with your Groq API key:

```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 3. Run the Server

```bash
python main.py
```

The server will start at `http://localhost:8000`

### 4. Test the API

**Option A: Swagger UI (Recommended)**
- Open `http://localhost:8000/docs` in your browser
- Interactive API documentation with "Try it out" buttons

**Option B: Automated Test Suite**
```bash
python test_api.py
```

**Option C: Interactive Testing**
```bash
python test_api.py interactive
```

**Option D: cURL**
```bash
curl -X POST "http://localhost:8000/api/ticket" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "I cannot login and was charged twice",
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

## 📊 API Endpoints

### Create Ticket
**POST** `/api/ticket`

```json
{
  "query": "I can't access my account and was charged twice",
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Response:**
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

### Get Tickets by Email
**GET** `/api/tickets/{email}`

Returns all tickets for a specific email address.

### Get All Tickets
**GET** `/api/tickets`

Returns all tickets (for testing/admin).

### Get Ticket by ID
**GET** `/api/ticket/{ticket_id}`

Returns a specific ticket.

### Health Check
**GET** `/health`

Server health status.

## 🧠 How It Works

### LangGraph Workflow

```
User Query → [Classify Problem] → Is NONE? → Yes → End
                    ↓
                    No
                    ↓
            [Classify Priority]
                    ↓
            [Create Ticket(s)] → Database
                    ↓
                   End
```

### Problem Types
- **Technical**: System errors, bugs, outages
- **Billing**: Payment issues, charges, refunds
- **Account**: Login, password, profile issues
- **General**: Feature questions, how-to guides
- **NONE**: Off-topic, spam

### Priority Levels

**HIGH** (2 hour response):
- Complete service outage
- Security breach
- Critical payment errors
- Data loss

**MEDIUM** (24 hour response):
- Partial disruptions with workarounds
- Billing inquiries
- Account access issues

**LOW** (48 hour response):
- General questions
- Minor UI issues
- Documentation requests

## 📝 Database Schema

```sql
CREATE TABLE tickets (
    id TEXT PRIMARY KEY,              -- UUID
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    query TEXT NOT NULL,
    problem_type TEXT NOT NULL,       -- Technical/Billing/Account/General
    priority TEXT NOT NULL,           -- HIGH/MEDIUM/LOW
    estimated_response_time TEXT,     -- "2 hours", "24 hours", "48 hours"
    created_at TIMESTAMP NOT NULL
);
```

## 🧪 Testing Examples

### Test Case 1: Single Problem
```python
Query: "I can't login to my account"
Result: 1 ticket (Account, HIGH)
```

### Test Case 2: Multiple Problems
```python
Query: "The system is down and I was charged twice!"
Result: 2 tickets (Technical-HIGH, Billing-MEDIUM)
```

### Test Case 3: Invalid Query
```python
Query: "Buy cheap watches now!"
Result: Error - "Your query doesn't match our support categories"
```

## 🔧 Environment Variables

```bash
GROQ_API_KEY=your_groq_api_key_here
```

## 📦 Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **langchain**: LLM framework
- **langchain-groq**: Groq integration
- **langgraph**: Workflow orchestration
- **pydantic**: Data validation
- **sqlite3**: Database (built-in)

## 🎨 Customization

### Modify Priority Logic
Edit `agent/nodes.py` → `classify_priority_node()`

### Add New Problem Types
Update the prompt in `agent/nodes.py` → `classify_problem_node()`

### Change Response Times
Edit `agent/nodes.py` → `create_tickets_node()` → `response_times` dict

### Add New Endpoints
Add routes in `main.py`

## 📚 Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🐛 Troubleshooting

**"GROQ_API_KEY not found"**
- Create `.env` file with your API key

**"Model not found: openai/gpt-oss-120b"**
- Check if model name is correct in Groq's documentation
- Alternative models: `mixtral-8x7b-32768`, `llama3-70b-8192`

**"Database locked"**
- Close any other connections to `tickets.db`
- Delete `tickets.db` and restart

## 📄 License

MIT License

## 🤝 Contributing

Feel free to submit issues and pull requests!

---

**Built with ❤️ using LangGraph + FastAPI + Groq**
