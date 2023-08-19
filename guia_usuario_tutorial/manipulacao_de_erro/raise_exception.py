from fastapi import FastAPI, HTTPException


app = FastAPI()


items = {"foo": "The foo Wrestlers"}


# lançando uma exception com HTTPException
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
