from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

@app.get("/")
def home():
    return {"message": "Welcome to the User API!"}

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def add_user(user: User):
    users.append(user.dict()) 
    return {"message": "User added successfully!", "user": user}
