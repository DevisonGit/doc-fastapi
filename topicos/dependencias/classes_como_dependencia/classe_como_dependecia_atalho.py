from fastapi import FastAPI, Depends
from typing import Annotated


app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


# classe como dependência
@app.get("/items/")
async def read_items(commonos: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commonos.q:
        response.update({"q": commonos.q})
    items = fake_items_db[commonos.skip: commonos.skip + commonos.limit]
    response.update({"items": items})
    return response
