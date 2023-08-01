from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


# criando uma exception
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


# manipulador da exception customizada
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=418, content={"message": f"Oops! {exc.name} did something. There goes a rainbow"})


@app.get("/unicorns/{name}")
async def read_item(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"name": name}
