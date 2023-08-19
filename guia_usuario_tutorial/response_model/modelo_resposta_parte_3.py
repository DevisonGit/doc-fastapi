from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": "There goes my baz", "price": 50.2, "tax": 10.5, "tags": []},
}


# o response_model_exclude_unset igual a true só exibe os campos preenchidos os defaults são ignorados
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# o response_model_include monta um modelo personalizado, com os atributos do modelo
@app.get("/items/{item_id}/name/", response_model=Item, response_model_include={"name", "description"})
async def read_item_name(item_id: str):
    return items[item_id]


# o response_model_exclude exclui um atributo do modelo
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public(item_id: str):
    return items[item_id]
