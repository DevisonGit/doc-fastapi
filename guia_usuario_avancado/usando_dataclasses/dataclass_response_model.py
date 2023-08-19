from dataclasses import dataclass, field
from fastapi import FastAPI
from typing import List


@dataclass
class Item:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    description: str | None = None
    tax: float | None = None


app = FastAPI()


@app.get("/items/next", response_model=Item)
async def read_next_item():
    return{
        "name": "Island in the Moon",
        "price": 12.99,
        "description": "a place to be playin' and havin' fun",
        "tags": ["breater"]
    }
