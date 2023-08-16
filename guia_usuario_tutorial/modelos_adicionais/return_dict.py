from typing import Dict
from fastapi import FastAPI

app = FastAPI()


# retornando um Dict str:float
@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 14.45, "bar": 15}
