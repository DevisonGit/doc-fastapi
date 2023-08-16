from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI()


# implementa um response usando o orjson que é mais rapido
@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])
