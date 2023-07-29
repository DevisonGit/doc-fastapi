from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class Car(BaseItem):
    type: str = "Car"


class Plane(BaseItem):
    type: str = "Plane"


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


# usando o Union para informar que o retorno pode ser qualquer um dos modelos
@app.get("/items/{item_id}", response_model=Union[Car, Plane])
async def read_item(item_id: str):
    return items[item_id]