from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Set, Union


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


# definindo uma tags que sera usada pela documentação para segmetar por tags
@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item


@app.get("/items/", response_model=list[Item], tags=["items"])
async def read_items():
    return [{"name": "foo", "price": 42.5}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "jonhdoe"}]
