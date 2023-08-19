from fastapi import FastAPI
from pydantic import BaseModel
from typing import  Set


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: Set[str] = set()


# description aparecera na documetação
@app.post("/items/", response_model=Item, summary="Create an item",
          description=" Create an item with all the information name, description, price, tax and tags")
async def create_item(item: Item):
    return item
