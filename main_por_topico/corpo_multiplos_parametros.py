from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# podemos definir um valor padrão para o parametro de corpo
@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(title="The id of the item to get", ge=0, le=1000),
    q: str | None = None,
    item: Item | None = None,
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})
    return result


# declarando multiplos parametros de corpo
@app.put("/items/multiplos/{item_id}")
async def update_item_multiplos(item_id: int, item: Item, user:User):
    result = {"item_id": item_id, "item": item, "user": user}
    return result


# valores singulares no corpo
@app.put("/items/singular/{item_id}")
async def update_item_singular(item_id: int, item: Item, user: User, importance: int = Body()):
    result = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return result


# multiplos parametros de corpo e consulta
@app.put("/items/corpo/{item_id}")
async def update_item_corpo(item_id: int, item: Item, user: User, importance: int = Body(), q: str | None = None):
    result = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        result.update({"q": q})
    return result


# unico parametro de corpo indicando sua chave
@app.put("/items/chave/{item_id}")
async def update_item_chave(item_id: int, item: Item = Body(embed=True)):
    result = {"item_id": item_id, "item": item}
    return result
