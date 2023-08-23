from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

items = {}


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "fighters"}
    items["bar"] = {"name": "Tenders"}


@app.on_event("shutdown")
async def shutdown_event():
    items.clear()
    items["baz"] = {"name": "shut"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]


# testa o startup
def test_read_items():
    with TestClient(app) as client:
        response = client.get("/items/foo")
        assert response.status_code == 200
        assert response.json() == {"name": "fighters"}


# testa o shutdown
def test_close_items():
    with TestClient(app) as client:
        pass
    assert items == {"baz": {"name": "shut"}}
