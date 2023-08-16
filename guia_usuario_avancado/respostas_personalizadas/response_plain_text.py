from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()


# retornar um texto ou bytes simples
@app.get("/", response_class=PlainTextResponse)
async def main():
    return "hello hello world"
