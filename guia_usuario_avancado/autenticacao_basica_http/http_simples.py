from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}

