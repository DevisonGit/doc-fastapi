from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


# parametro da rota da url
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# parametro da rota da url com tipo, gera erro se o tipo passado não for do tipo int
@app.get("/items/int/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# em rotas fixas a ordem importa, para o /user/me não coincidir com /users/{user_id}, ela deve vir antes.
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user_id(user_id):
    return {"user_id": user_id}


# valores predefinidos da classe Enum
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW!"}
    if model_name == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# podemos ter rotas que recebem um path como parametro
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
