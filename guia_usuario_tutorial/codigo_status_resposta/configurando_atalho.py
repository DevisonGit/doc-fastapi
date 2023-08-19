from fastapi import FastAPI, status


app = FastAPI()


# configurando o status code, utilizando um atalho para lembrar o o significado do codigo
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: str):
    return item
