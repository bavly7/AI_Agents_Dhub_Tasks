# 🚀 Setup Guide - Customer Support Ticket System

## Step-by-Step Installation

### 1️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- FastAPI & Uvicorn (web server)
- LangChain & LangGraph (AI workflow)
- Groq integration
- Pydantic (data validation)

### 2️⃣ Get Your Groq API Key

1. Go to https://console.groq.com
2. Sign up or login
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `gsk_...`)

### 3️⃣ Configure Environment

Open the `.env` file and add your API key:

```bash
GROQ_API_KEY=gsk_your_actual_key_here
```

**Important**: Replace `gsk_your_actual_key_here` with your real key!

### 4️⃣ Verify Setup

Check if everything is ready:

```bash
python -c "import fastapi, langchain, langgraph; print('✅ All dependencies installed!')"
```

### 5️⃣ Start the Server

```bash
python main.py
```

You should see:
```
🚀 Starting Customer Support Ticket System...
📝 API Documentation: http://localhost:8000/docs
🔄 Interactive API: http://localhost:8000/redoc
```

### 6️⃣ Test the System

**Option 1: Use Swagger UI (Easiest)**
1. Open your browser
2. Go to: http://localhost:8000/docs
3. Click on "POST /api/ticket"
4. Click "Try it out"
5. Enter test data:
```json
{
  "query": "I can't login to my account",
  "name": "Test User",
  "email": "test@example.com"
}
```
6. Click "Execute"
7. See the response!

**Option 2: Run Automated Tests**
```bash
python test_api.py
```

**Option 3: Interactive Testing**
```bash
python test_api.py interactive
```

## 📊 What to Expect

### Single Problem Example
**Input:**
```json
{
  "query": "I forgot my password",
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Output:**
```json
{
  "success": true,
  "message": "Successfully created 1 ticket(s)",
  "tickets": [
    {
      "ticket_id": "a1b2c3d4-...",
      "problem_type": "Account",
      "priority": "MEDIUM",
      "estimated_response_time": "24 hours"
    }
  ]
}
```

### Multiple Problems Example
**Input:**
```json
{
  "query": "The system is down and I was charged twice!",
  "name": "Jane Smith",
  "email": "jane@example.com"
}
```

**Output:**
```json
{
  "success": true,
  "message": "Successfully created 2 ticket(s)",
  "tickets": [
    {
      "ticket_id": "e5f6g7h8-...",
      "problem_type": "Technical",
      "priority": "HIGH",
      "estimated_response_time": "2 hours"
    },
    {
      "ticket_id": "i9j0k1l2-...",
      "problem_type": "Billing",
      "priority": "MEDIUM",
      "estimated_response_time": "24 hours"
    }
  ]
}
```

## 🔍 Viewing Your Tickets

### Get all tickets for an email:
```bash
curl http://localhost:8000/api/tickets/john@example.com
```

Or visit: http://localhost:8000/docs and use the GET endpoint

### View all tickets (testing):
```bash
curl http://localhost:8000/api/tickets
```

## 🐛 Troubleshooting

### Problem: "GROQ_API_KEY not found"
**Solution**: Make sure you created `.env` file with your API key

### Problem: "No module named 'fastapi'"
**Solution**: Run `pip install -r requirements.txt`

### Problem: "Address already in use"
**Solution**: Another process is using port 8000. Either:
- Stop that process
- Or change port in `main.py`: `uvicorn.run(app, port=8001)`

### Problem: LLM returns invalid JSON
**Solution**: This is rare but can happen. The code has fallback logic. If persistent, try a different query format.

### Problem: "Model not found: openai/gpt-oss-120b"
**Solution**: The model name might have changed. Check Groq's docs and update in `agent/nodes.py`:
```python
return ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",  # or another available model
    temperature=0
)
```

## 🎯 Quick Test Commands

```bash
# Test 1: Simple account issue
curl -X POST "http://localhost:8000/api/ticket" \
  -H "Content-Type: application/json" \
  -d '{"query": "I forgot my password", "name": "Test", "email": "test@test.com"}'

# Test 2: Multiple issues
curl -X POST "http://localhost:8000/api/ticket" \
  -H "Content-Type: application/json" \
  -d '{"query": "System is down and was charged twice", "name": "Test", "email": "test@test.com"}'

# Test 3: Get tickets
curl "http://localhost:8000/api/tickets/test@test.com"
```

## 📁 Files Overview

- `main.py` - FastAPI server & endpoints
- `database.py` - SQLite database operations
- `agent/agent.py` - LangGraph workflow orchestration
- `agent/nodes.py` - AI classification logic
- `agent/edges.py` - Routing between nodes
- `test_api.py` - Testing scripts
- `.env` - Your API key (never commit this!)
- `tickets.db` - SQLite database (auto-created)

## 🎉 Success Checklist

- [ ] Dependencies installed
- [ ] Groq API key configured in `.env`
- [ ] Server starts without errors
- [ ] Swagger UI accessible at http://localhost:8000/docs
- [ ] Test ticket created successfully
- [ ] Tickets saved in database
- [ ] Can retrieve tickets by email

## 🚀 Next Steps

1. Try different query types
2. Test edge cases (spam, multiple issues)
3. Check the database: `sqlite3 tickets.db "SELECT * FROM tickets;"`
4. Modify priority logic in `agent/nodes.py`
5. Add custom problem types
6. Build a frontend!

---

**Need Help?** Check the main README.md or review the code comments.

**Happy Testing! 🎯**
