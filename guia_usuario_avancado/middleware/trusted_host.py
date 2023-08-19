from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()


app.add_middleware(TrustedHostMiddleware, allowed_hosts=["exemplo.com", "*.exemplo.com"])


@app.get("/")
async def main():
    return {"message": "hello moto"}
