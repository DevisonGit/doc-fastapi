from fastapi import FastAPI, APIRouter

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"item_id": "foo"}]


# usando o nome da função com operation_id
def use_route_names_as_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRouter):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)
