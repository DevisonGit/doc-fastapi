from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


# faz um redirecionamento
@app.get("/typer", response_class=RedirectResponse)
async def redirect_typer():
    return "https://typer.tiangolo.com"
