import sqlite3
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Database:
    def __init__(self, db_path: str = "tickets.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Initialize the database with the tickets table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                query TEXT NOT NULL,
                problem_type TEXT NOT NULL,
                priority TEXT NOT NULL,
                estimated_response_time TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def create_ticket(self, name: str, email: str, query: str,
                     problem_type: str, priority: str,
                     estimated_response_time: str) -> str:
        """Create a new ticket and return its UUID"""
        ticket_id = str(uuid.uuid4())
        created_at = datetime.utcnow().isoformat()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tickets (id, name, email, query, problem_type, priority,
                               estimated_response_time, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (ticket_id, name, email, query, problem_type, priority,
              estimated_response_time, created_at))

        conn.commit()
        conn.close()

        return ticket_id

    def get_ticket_by_id(self, ticket_id: str) -> Optional[Dict]:
        """Retrieve a ticket by ID"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return dict(row)
        return None

    def get_tickets_by_email(self, email: str) -> List[Dict]:
        """Retrieve all tickets for a given email"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tickets WHERE email = ? ORDER BY created_at DESC",
                      (email,))
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def get_all_tickets(self) -> List[Dict]:
        """Retrieve all tickets (for testing)"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tickets ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]


# Initialize database on import
db = Database()
