from fastapi import FastAPI

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


# cria um sub app que na verdade é outro app FastAPI
subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


# monta o sub app
app.mount("/subapi", subapi)
