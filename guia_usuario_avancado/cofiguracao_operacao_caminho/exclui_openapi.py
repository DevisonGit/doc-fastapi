from fastapi import FastAPI, APIRouter

app = FastAPI()


# exclui da openAPI, mas operação funciona normalmente
@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "foo"}]
