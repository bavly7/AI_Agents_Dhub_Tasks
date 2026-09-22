from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List
import uvicorn
from agent import process_ticket_request
from database import db

# Initialize FastAPI app
app = FastAPI(
    title="Customer Support Ticket System",
    description="AI-powered ticket routing system with LangGraph",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request models
class TicketRequest(BaseModel):
    query: str
    name: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "query": "I can't login to my account and I was charged twice",
                "name": "John Doe",
                "email": "john@example.com"
            }
        }


class TicketResponse(BaseModel):
    success: bool
    message: str
    tickets: List[dict] = []


# Endpoints
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Customer Support Ticket System API",
        "version": "1.0.0",
        "endpoints": {
            "create_ticket": "POST /api/ticket",
            "get_tickets_by_email": "GET /api/tickets/{email}",
            "get_all_tickets": "GET /api/tickets",
            "docs": "GET /docs"
        }
    }


@app.post("/api/ticket", response_model=TicketResponse)
async def create_ticket(request: TicketRequest):
    """
    Create a support ticket by analyzing the query with LangGraph.

    The system will:
    1. Classify the problem type(s) (Technical, Billing, Account, General, or NONE)
    2. Determine priority (HIGH, MEDIUM, LOW) for each problem
    3. Create separate tickets for each problem type detected
    4. Return ticket IDs and estimated response times

    **Note:** A single query can generate multiple tickets if it contains multiple issues.
    """
    try:
        result = process_ticket_request(
            query=request.query,
            name=request.name,
            email=request.email
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing ticket: {str(e)}")


@app.get("/api/tickets/{email}")
async def get_tickets_by_email(email: str):
    """
    Retrieve all tickets for a specific email address.

    Returns tickets in reverse chronological order (newest first).
    """
    try:
        tickets = db.get_tickets_by_email(email)
        return {
            "success": True,
            "count": len(tickets),
            "tickets": tickets
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving tickets: {str(e)}")


@app.get("/api/tickets")
async def get_all_tickets():
    """
    Retrieve all tickets in the system (for testing purposes).

    Returns tickets in reverse chronological order (newest first).
    """
    try:
        tickets = db.get_all_tickets()
        return {
            "success": True,
            "count": len(tickets),
            "tickets": tickets
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving tickets: {str(e)}")


@app.get("/api/ticket/{ticket_id}")
async def get_ticket_by_id(ticket_id: str):
    """
    Retrieve a specific ticket by its ID.
    """
    try:
        ticket = db.get_ticket_by_id(ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return {
            "success": True,
            "ticket": ticket
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving ticket: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": "2026-09-22T15:12:07.175Z"}


if __name__ == "__main__":
    print("🚀 Starting Customer Support Ticket System...")
    print("📝 API Documentation: http://localhost:8000/docs")
    print("🔄 Interactive API: http://localhost:8000/redoc")
    print("\n💡 Test the API using:")
    print("   - Swagger UI at /docs")
    print("   - test_api.py script")
    print("   - cURL commands (see README)\n")

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
