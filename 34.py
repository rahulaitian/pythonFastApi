import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE name = ?", ("Rahul",))

conn.commit()
conn.close()
print("Record updated successfully!")