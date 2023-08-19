from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from typing import Annotated


app = FastAPI()


items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
async def upsert_item(item_id: str, name: Annotated[str, Body()] = None, size: Annotated[int, Body()] = None):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
