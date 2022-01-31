from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User

app = FastAPI()

# Mock a database filled with users.
users: List[User] = [
  User(
    id=UUID("808fd3fb-d3b5-4ec0-abdc-c86b8109e443"), 
    first_name="Sasuke", 
    last_name="Uchiha", 
    gender=Gender.male, 
    roles=[Role.admin]
  ),
  User(
    id=UUID("5d1cb42e-304b-4168-814b-1beb21617fdc"), 
    first_name="Naruto", 
    last_name="Uzumaki", 
    gender=Gender.male, 
    roles=[Role.student]
    )
]

@app.get("/")
async def root():
  return {"message": "Hello world!"}

@app.get("/api/v1/users")
async def get_users():
  return users

@app.post("/api/v1/users")
async def post_user(user: User):
  users.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
  for user in users:
    if user.id == id:
      users.remove(user)
      return
  raise HTTPException(
    status_code=404,
    detail=f"user with id: {id} doesn't exists"
  )
