from dataclasses import dataclass
from fastapi import FastAPI


# usa o data class que entre outra coisas gera o __init__() automaticamente
@dataclass
class Item:
    name: str
    price: float
    description: str | None = None
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
