from fastapi import FastAPI, Depends
from typing import Annotated


app = FastAPI()


# função para parametros em comum
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"common": {"q": q, "skip": skip, "limit": limit}}


# usando a dependencia para utilizar parametros em comum
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# usando a dependencia para utilizar parametros em comum
@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
