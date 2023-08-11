from typing import Annotated, Any

from fastapi import Depends, FastAPI


def generate_dep_a():
    print("A")


def generate_dep_b():
    print("B")


def generate_dep_c():
    print("C")


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        print("fim A")


async def dependency_b(dep_a: Annotated[Any, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        print("fim B")


async def dependency_c(dep_b: Annotated[Any, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        print("fim C")


app = FastAPI()


@app.get("/items/", dependencies=[Depends(dependency_c)])
async def read_items():
    return "rodou"
