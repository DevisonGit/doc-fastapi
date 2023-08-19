from fastapi import FastAPI, Request

app = FastAPI()


# usando o request diretamente para acessar o ip
@app.get("/items/{item_id}")
async def read_items(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}
