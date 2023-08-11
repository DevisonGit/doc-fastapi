from fastapi import FastAPI, Form


app = FastAPI()


# usando o Form para pegar os dados de um formulario ao inves de Json
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
