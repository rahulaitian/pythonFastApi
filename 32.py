import sqlite3


conn = sqlite3.connect("example.db")
cursor = conn.cursor()

users = [
    ("Rahul", 25, "r@examplew.com"),
    ("CHaitanya", 22, "c@examplwe.com"),
    ("Prateek", 23, "p@examwple.com")
]

cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users)
conn.commit()
conn.close()

print("Multiple records inserted successfully!")
