from fastapi import FastAPI, HTTPException
from schemas import User
from another import Address

app = FastAPI()
users = []
addresses = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/address")
def get_address():
    return addresses

@app.post("/api/users", status_code=201)
def add_user(user: User):
    users.append(user)
    return user

@app.post("/api/address", status_code=201)
def add_address(address: Address):
    addresses.append(address)
    return address