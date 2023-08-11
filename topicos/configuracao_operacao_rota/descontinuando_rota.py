from fastapi import FastAPI


app = FastAPI()


@app.get("/items/", tags=["items"])
async def read_item():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


# descontinuando uma rota
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
