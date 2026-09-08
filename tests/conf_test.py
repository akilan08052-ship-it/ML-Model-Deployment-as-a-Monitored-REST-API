from app.main import  app
from fastapi.testclient import TestClient







def test_root():
    with TestClient(app) as client:
        response=client.get("api/v1/")
        assert response.status_code==200 
        assert response.json()=={"message":"ML API is live"}
def test_predict():
    with TestClient(app) as client:
        response_v1=client.post("api/v1/predict"   ,json={
        "sepallength": 6.3,
        "sepalwidth": 3.3,
        "petallength": 6.0,
        "petalwidth": 2.5
    })
        response_v2=client.post("api/v2/predict"  ,json={
            "sepallength": 6.3,
            "sepalwidth": 3.3,
            "petallength": 6.0,
            "petalwidth": 2.5
            })
               
        
        data_v1=response_v1.json()
        data_v2=response_v2.json()
        
        assert response_v1 and response_v2.status_code==200 
        assert data_v1["species"] and data_v1["species"]=="Iris-virginica"
        assert data_v1['accuracy'] and data_v1["accuracy"]==1.0
        assert 'model_type' not in data_v1
        assert 'model_type' in data_v2
        assert 'request_id' in data_v1 and data_v2
        
def test_predict_batch():
    with TestClient(app) as client:
        response=client.post("api/v1/batch-prediction",json={
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
        })
        data=response.json()
        assert response.status_code==200
        assert data["predictions"][0]["species"] == "Iris-setosa"
        assert data["predictions"][0]["accuracy"] == 1.0

        assert data["predictions"][1]["species"] == "Iris-virginica"
        assert data["predictions"][1]["accuracy"] == 1.0

        assert "request_id" in data["predictions"][0]
        assert "request_id" in data["predictions"][1]

def test_health():
    with TestClient(app) as client:
        response=client.get("api/v1/health")
        response.status_code=200
        data=response.json()
        assert data["status"]=="Prediction service is Available" 
        assert 'request_id' in data

def test_model_info():
     with TestClient(app) as client:
        
        response=client.get("api/v1/model-info")
        data=response.json()
        response.status_code=200
        assert 'model_type' in data

        assert 'trained_date' in data



            






