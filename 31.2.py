import sqlite3
import os

# Connect to SQLite database
db_path = "example.db"  # Change this if using a different database file
absolute_path = os.path.abspath(db_path)

print("Database file location:", absolute_path)
