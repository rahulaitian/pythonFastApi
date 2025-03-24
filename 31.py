import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table named 'users'
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Table created successfully!")
