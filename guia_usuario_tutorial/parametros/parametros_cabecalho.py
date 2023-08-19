from fastapi import FastAPI, Header, Cookie

app = FastAPI()


# usando o Header para pegar parametros do cabeçalho
@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None),
                     strange_header: str | None = Header(default=None, convert_underscores=False),
                     x_token: list[str] | None = Header(default=None)
                     ):
    return {"user-agent": user_agent, "strange_header": strange_header, "x-token values": x_token}
