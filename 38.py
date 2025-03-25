from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional

app = FastAPI()

# Dummy user storage
users = []

# Authentication Dependency
def verify_authentication(api_key: Optional[str] = Header(None)):
    print(f"Received API Key: {api_key}")
    if api_key != "my-secret-key":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key

# Root (No authentication needed)
@app.get("/")
def home():
    return {"message": "Welcome to the Secure User API!"}

# Protected GET API
@app.get("/users")
def get_users(api_key: str = Depends(verify_authentication)):
    return {"users": users}

# Protected POST API
@app.post("/users")
def add_user(user: dict, api_key: str = Depends(verify_authentication)):
    users.append(user)
    return {"message": "User added successfully!", "user": user}
