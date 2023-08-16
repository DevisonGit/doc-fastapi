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


# definindo modelo de resposta e codigo de retorno
@app.post("/items/", response_model=Item, status_code=status.HTTP_404_NOT_FOUND)
async def create_item(item: Item):
    return item
