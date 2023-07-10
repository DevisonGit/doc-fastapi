from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    chocolate = "chocolate"
    biscoito = "biscoito"
    caramelo = "caramelo"


app = FastAPI()

fake_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# Parametros da consulta
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # skip e limit
    return fake_db[skip: skip + limit]


# Parametros da consulta opcionais
@app.get("/items/opcional/{item_id}")
async def read_item_op(item_id: str, q: str | None = None):  # q é opcional e valor padrão é None
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}


# Conversão de tipo bool
@app.get("/items/bool/{item_id}")
async def read_item_bool(item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


# Multimplos parametros de rota e consulta
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


# Parametros de consulta obrigatorios
@app.get("/items/{item_id}")
async def read_item_obrigatorio(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}


# Mix obrigatorio, valor padrão e opcionais
@app.get("/items/mix/{item_id}")
async def read_mix(item_id: int, needy: str, skip: int = 0, limit: int | None = None):
    return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}


# Usando Enum com parâmetro de consulta
@app.get("/items/enum/")
async def read_items_enum(twix: ModelName):
    return {"twix": twix}
