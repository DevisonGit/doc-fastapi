from fastapi import FastAPI, Query
from typing import Union, List

app = FastAPI()


# validando se recebemos o parametro de consulta
@app.get("/items/")
async def read_item(q: Union[str, None] = None):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# validando seu tamanho, defindo o minimo de 3 e maximo 50 caracteres
@app.get("/items/tamanho/")
async def read_item_tamanho(q: str = Query(default=None, min_length=3, max_length=50)):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Adicionando expressões regulares
@app.get("/items/expressoes/")
async def read_item_expressoes(q: str = Query(default=None, pattern="^fixedquery$")):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Valor padrão
@app.get("/items/valor/padrao")
async def read_item_valor_padrao(q: str = Query(default="fixedquery", min_length=3)):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Valor Obrigatorio
@app.get("/items/valor/obrigatorio")
async def read_item_valor_obrigatorio(q: str = Query(min_length=3)):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Lista de parametros de consulta usando List do typing
@app.get("/items/lista/typing")
async def read_item_list(q: Union[List[str], None] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# Lista de parametros de consulta usando o list
@app.get("/items/lista/")
async def read_item_list(q: list = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# Adicionando metadados
@app.get("/item/metadados")
async def read_item_metadados(
        q: str = Query(
            default=None,
            title="query string",
            description="Query string for the items to search in the database that have a good match",
        )):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Alias
@app.get("/items/alias/")
async def read_item_alias(q: str = Query(default=None, alias="item-query")):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Parametros descontinuados
@app.get("/items/descontinuado/")
async def read_item_descontinuado(q: str = Query(default=None, deprecated=True)):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result
