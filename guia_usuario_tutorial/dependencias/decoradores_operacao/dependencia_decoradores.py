from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Annotated


app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake_super_secret_token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake_super_secret_key":
        raise HTTPException(status_code=400, detail="x-Key header invalid")


# dependencias no decorator
@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
