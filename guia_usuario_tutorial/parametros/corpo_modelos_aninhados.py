from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl
from typing import Union, List, Set, Dict

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl  # tipos especiais de validação (Valida se é uma url )
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags_list: List[str] = []  # definindo campo do tipo lista de string
    tags_set: Set[str] = set()  # definindo um set (não é permitido dados duplicados)
    imagem: Union[Image, None] = None  # definindo um modelo aninhado
    images: Union[List[Image], None] = None  # definindo uma lista de submodelos


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]  # usando modelos profundamente aninhado


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


# no corpo da requisição deve vir uma de lista pura, com modelos image
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


# espera um dict de chave int e valor float
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
