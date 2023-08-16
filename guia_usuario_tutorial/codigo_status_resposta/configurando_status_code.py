from fastapi import FastAPI


app = FastAPI()


# configurando o status code
@app.post("/items/", status_code=201)
async def create_item(item: str):
    return item


