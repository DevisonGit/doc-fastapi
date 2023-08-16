from fastapi import FastAPI
from enum import Enum


app = FastAPI()


# classe Enum
class Tags(Enum):
    items = "items"
    users = "users"


# definindo uma tags usando o Enum
@app.get("/items/", tags=[Tags.items])
async def read_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]
