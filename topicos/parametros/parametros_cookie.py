from typing import Union
from fastapi import Cookie, FastAPI

app = FastAPI()


# usando parametros de cookie
@app.get("/items/")
async def read_items(asd_id: Union[str, None] = Cookie(default=None)):
    return {"asd_id": asd_id}
