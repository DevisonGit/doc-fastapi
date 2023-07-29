from fastapi import FastAPI, Path, Query

app = FastAPI()


# Validando parametro de rota
@app.get("/items/{item_id}")
async def read_item(
        item_id: int = Path(title="The ID of the item to get"),
        q: str = Query(default=None, alias="item-query")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# validações numericas ge é igual a >=
@app.get("/items/ge/{item_id}")
async def read_item_numerico_ge(item_id: int = Path(title="The ID of the item to get", ge=1)):
    return {"item_id": item_id}


# validações numericas gt é igual a >
@app.get("/items/gt/{item_id}")
async def read_item_numerico_gt(item_id: int = Path(title="The ID of the item to get", gt=1)):
    return {"item_id": item_id}


# validações numericas le é igual a <=
@app.get("/items/le/{item_id}")
async def read_item_numerico_le(item_id: int = Path(title="The ID of the item to get", le=10)):
    return {"item_id": item_id}


# validações numericas lt é igual a <
@app.get("/items/lt/{item_id}")
async def read_item_numerico_lt(item_id: int = Path(title="The ID of the item to get", lt=1)):
    return {"item_id": item_id}


# validações numericas de float
@app.get("/items/float/{item_id}")
async def read_item_float(item_id: float = Path(title="The id of the item get", gt=0, lt=5.5)):
    return {"item_id": item_id}
