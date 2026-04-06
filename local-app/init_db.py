import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("registrations.db")
cursor = conn.cursor()

# Create registrations table
cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    department TEXT NOT NULL,
    batch TEXT NOT NULL,
    ku_id TEXT NOT NULL,
    enrollment_number TEXT NOT NULL,
    event_name TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")
