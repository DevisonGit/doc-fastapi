from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


# Corpo da requisição
@app.post("/items/")
async def create_item(item: Item):
    return item


# Usando o modelo
@app.post("/items/modelo/")
async def create_item_modelo(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Corpo da requisição + parametros de rota
@app.put("/items/{item_id}")
async def create_item_put(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


# Corpo da requisição + parametros de rota + parametros de consulta
@app.put("/items/{item_id}/all/")
async def create_item_all(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
