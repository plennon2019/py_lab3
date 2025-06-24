from fastapi import FastAPI, HTTPException
from schemas import User
from another import Address

app = FastAPI()
users = []
addresses = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]


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

@app.put("/api/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    return user

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return users.pop(user_id)

def delete_address(address_id: int):
    if address_id < 0 or address_id >= len(addresses):
        raise HTTPException(status_code=404, detail="Address not found")
    return addresses.pop(address_id)
