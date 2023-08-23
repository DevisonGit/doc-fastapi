from contextlib import asynccontextmanager
from fastapi.testclient import TestClient
from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}


def test_predict():
    with TestClient(app) as client:
        response = client.get("/predict?x=10")
        assert response.status_code == 200
        assert response.json() == {"result": 420.0}
    assert ml_models == {}
