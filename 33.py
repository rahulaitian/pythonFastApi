import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

print("record of all users")
for row in rows:
    print(row)
    cursor.close()