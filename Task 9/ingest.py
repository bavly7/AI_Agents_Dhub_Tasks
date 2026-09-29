import sqlite3

def init_db():
    conn = sqlite3.connect("wedding.db")
    cursor = conn.cursor()

    # Create Halls Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS halls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            capacity INTEGER,
            style TEXT,
            food TEXT,
            price REAL
        )
    ''')

    # Create Bookings Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hall_name TEXT,
            date TEXT,
            customer_name TEXT
        )
    ''')

    # Insert Dummy Halls
    halls_data = [
        ('Royal Ballroom', 500, 'Indoor Classic', 'Open Buffet', 50000),
        ('Gardenia View', 200, 'Outdoor Garden', 'Set Menu', 30000),
        ('Crystal Sky', 300, 'Indoor Modern', 'Open Buffet', 40000),
        ('Nile Breeze', 150, 'Outdoor Nile View', 'Custom Seafood', 25000)
    ]
    
    try:
        cursor.executemany('''
            INSERT INTO halls (name, capacity, style, food, price) 
            VALUES (?, ?, ?, ?, ?)
        ''', halls_data)
    except sqlite3.IntegrityError:
        print("Halls already exist. Skipping insertion.")

    # Insert Dummy Booking for conflict testing
    try:
        cursor.execute('''
            INSERT INTO bookings (hall_name, date, customer_name) 
            VALUES ('Gardenia View', '2026-10-15', 'Ahmed Ali')
        ''')
    except Exception as e:
        pass

    conn.commit()
    conn.close()
    print("Database built successfully with dummy data!")

if __name__ == "__main__":
    init_db()