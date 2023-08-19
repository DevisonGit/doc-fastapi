from fastapi import FastAPI, Depends
from typing import Annotated


app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"common": {"q": q, "skip": skip, "limit": limit}}


# colocando a dependecia em uma variavel e usando em varios lugares
CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons
