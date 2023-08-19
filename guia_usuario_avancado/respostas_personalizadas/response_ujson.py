from fastapi import FastAPI
from fastapi.responses import UJSONResponse


app = FastAPI()


# retornando um ujson
@app.get("/items", response_class=UJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]
