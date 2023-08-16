from typing import Annotated
from fastapi import Header, HTTPException, status


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-token header invalid")


async def get_query_token(token: str):
    if token != "tokoso":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No token provided")
