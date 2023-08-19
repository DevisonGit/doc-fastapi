from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


# faz um redirecionamento
@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")
