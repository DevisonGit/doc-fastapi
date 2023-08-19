from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


# usando redirect, com status_code diferente do padrão
@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"
