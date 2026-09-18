import httpx
from app.config import settings

BASE_URL="http://0.0.0.0:8000"


def test_health():
    response=httpx.get("http://localhost:8000/api/v1/",headers={"X-API-KEY":settings.API_KEY})
    assert response.status_code==200


def test_predict_batch():
    
    response=httpx.post("http://localhost:8000/api/v1/batch-prediction",json={
            "inputs":[{
                "sepallength":2.8,
                "sepalwidth":2.1,
                "petallength":1.4,
                "petalwidth":1.1

            },
            {
              "sepallength":6.3,
              "sepalwidth":2.1,
              "petallength":6.0,
              "petalwidth":2.5
            }]
    },headers={'X-API-KEY':settings.API_KEY})
    
    assert response.status_code==200

TRAGET_URL="http://localhost:8000/api/v1/batch-prediction"
TOTAL_REQUEST=100
TOTAL_USERS=10




