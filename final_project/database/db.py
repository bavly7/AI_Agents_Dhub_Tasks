import sqlite3

def create_connection():
    conn = sqlite3.connect("leads.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            url TEXT UNIQUE,
            email TEXT,
            is_qualified BOOLEAN,
            email_sent BOOLEAN DEFAULT 0,
            reason TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_lead(lead: dict):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO leads (company_name, url)
        VALUES (?, ?)
    """, (lead["company_name"], lead["url"]))
    conn.commit()
    conn.close()

def get_unprocessed_leads():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads WHERE is_qualified IS NULL")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_qualified_leads():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads WHERE is_qualified = 1 AND email_sent = 0")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def update_lead(id, is_qualified, email=None, reason=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE leads SET is_qualified=?, email=?, reason=?
        WHERE id=?
    """, (is_qualified, email, reason, id))
    conn.commit()
    conn.close()

def mark_email_sent(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE leads SET email_sent=1 WHERE id=?", (id,))
    conn.commit()
    conn.close()