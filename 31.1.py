import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")

table_exists = cursor.fetchone()

if table_exists:
    print("Table 'users' exists.")
else:
    print("Table 'users' does not exist.")

conn.close()
