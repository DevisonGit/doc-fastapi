from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


# definindo um modelo de retorno para a função
@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="portal gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


# definindo o modelo usando o response_model
@app.post("/items/response/model/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/items/response/model/", response_model=list[Item])
async def read_items():
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


# não fazer isso em produção, estamos retornando dados sensivel
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user


# quando tivermos dados sensiveis podemos retornar um outro tipo de modelo
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user

