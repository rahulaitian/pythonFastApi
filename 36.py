from fastapi import FastAPI

app = FastAPI()
users = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 22, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 23, "email": "charlie@example.com"},
]
@app.get("/users")
def get_users():
    return {"users": users}