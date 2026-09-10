from app.main import  app
from app.config import settings
from fastapi.testclient import TestClient
from fastapi.requests import Request


def test_missing_api_key():
    with TestClient(app) as client:
        response=client.post("api/v1/predict",json={
            "sepallength": 6.3,
            "sepalwidth": 3.3,
            "petallength": 6.0,
            "petalwidth": 2.5
        })
        data=response.json()
        assert response.status_code==401
        assert data["detail"]=="api key is required "

def test_invalid_api_key():
    with TestClient(app) as client:
        response=client.post("api/v1/predict",json={
            "sepallength": 6.3,
            "sepalwidth": 3.3,
            "petallength": 6.0,
            "petalwidth": 2.5
        },headers={"X-API-KEY":"worng api key"})
        data=response.json()
        assert response.status_code==401
        assert data["detail"]=="api key is invalid"

        