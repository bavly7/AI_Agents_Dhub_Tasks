from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
import sqlite3
import os

DB_PATH = "database/schedule.db"


class SchedulerInput(BaseModel):
    action: str = Field(description="Must be 'create' or 'delete'")
    event_name: str = Field(default=None, description="Name of the event (e.g., 'Team Meeting')")
    date: str = Field(default=None, description="Date in YYYY-MM-DD format")
    time: str = Field(default=None, description="Time in HH:MM format")

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(date, time)
        )
    """)
    conn.commit()
    conn.close()

def schedule_management_tool(action: str, event_name: Optional[str] = None, date: Optional[str] = None, time: Optional[str] = None) -> Dict[str, Any]:
    """Manages events: create, update, delete, and checks for conflicts using SQLite."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    action = action.lower()
    
    try:
        if action == "create":
            if not all([event_name, date, time]):
                return {"error": "Missing parameters (event_name, date, time) for creation."}
            

            cursor.execute("SELECT * FROM events WHERE date = ? AND time = ?", (date, time))
            if cursor.fetchone():
                conn.close()
                return {"status": "conflict", "message": f"Conflict! An event is already scheduled at {time} on {date}."}
            
            cursor.execute("INSERT INTO events (event_name, date, time) VALUES (?, ?, ?)", (event_name, date, time))
            conn.commit()
            conn.close()
            return {"status": "success", "message": f"Event '{event_name}' created successfully for {date} at {time}."}
            
        elif action == "delete":
            if not all([date, time]):
                return {"error": "Date and time are required to delete an event."}
            
            cursor.execute("DELETE FROM events WHERE date = ? AND time = ?", (date, time))
            if cursor.rowcount == 0:
                conn.close()
                return {"status": "not_found", "message": f"No event found at {time} on {date} to delete."}
                
            conn.commit()
            conn.close()
            return {"status": "success", "message": f"Event at {time} on {date} deleted successfully."}
            
        else:
            conn.close()
            return {"error": f"Unknown action '{action}'. Use 'create' or 'delete'."}
            
    except Exception as e:
        conn.close()
        return {"error": str(e)}