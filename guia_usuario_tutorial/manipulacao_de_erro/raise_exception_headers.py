from fastapi import FastAPI, HTTPException


app = FastAPI()


items = {"foo": "the foo wrestler"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "Theres goes my error"})
    return {"item": items[item_id]}
