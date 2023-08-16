from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # fornece um exemplo para a documentação
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2
                }
            ]
        }

    }


class ItemField(BaseModel):
    # usando o Field para fornecer exemplo para a documentação
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item using Fields"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(examples=[3.2])


class ItemBody(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/fields/{item_id}")
async def update_item(item_id: int, item: ItemField):
    results = {"item_id": item_id, "item": item}
    return results


#  usando o Body para fornecer um exemplo para a documentação
@app.put("/items/body/{item_id}")
async def update_item(
        item_id: int,
        item: Annotated[
            ItemBody,
            Body(
                examples=[
                    {
                        "name": "Foo",
                        "description": "A very nice Item using Body",
                        "price": 35.4,
                        "tax": 3.2
                    }
                ]
            )
        ]):
    results = {"item_id": item_id, "item": item}
    return results
