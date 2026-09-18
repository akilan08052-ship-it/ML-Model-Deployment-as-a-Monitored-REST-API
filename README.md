# ML-Model-Deployment-as-a-Monitored-REST-API
## About Project
  REST API which serve the to predict the the species type of the iris flower using the length and width of sepal,petal of the flower.This Rest API is monitored from request to response for record the purpose of the breakage during the server is running.
-----
## Tech Stack
 - Python
 - FastAPI
 - Uvicorn
 - Pydantic
 - Scikit-learn
 - Swagger
 - Prometheus

-----
## Features
 - Predict the species of iris flower 
 - Predict batch of iris flower 
 - providels model information
 - Health status of the model 
 - Provides Swagger UI for documentation of API 
 - Customized mertices for moniter the endpoints
---

## Project Structure
The provide the information of the each module and structure of the  project.
```text
ML-Model-Deployment-as-a-Mointered-REST Api
|
|_app
| |_logs
| | |_app.log
| |_models 
| |  |_schemas.py
| |_routes
|   |_v1.py
|   |_v2.py
| |___init__.py
| |_config.py
| |_dependencies.py
| |_logging_config.py
| |_main.py
| |_metrices.py
|
|_ml
| |_saved_model
| |   |_model.pkl
| |   |_accuracy.pkl
| |   |_scaler.pkl
| |_iris.csv
| |_train.py
|
|_tests
| |_batch_load.py
| |_conf_test.py
| |_predict_load.py
| |_security_test.py
| |_test_integration.py
|
|_.dockerignore
|_.example.env
|_.gitignore
|_docker-compose.yml
|_dockerfile
|_README.md
|_requirements.txt

```

---

## Use this project 

### Git Clone
```bash
git clone "https://github.com/akilan08052-ship-it/ML-Model-Deployment-as-a-Monitored-REST-API.git"
```

### Create Environment 

```bash
python -m venv env
```

### Activate Environment

```bash
env\Scripts\Activate
```

### Install Requirements
```bash 
pip install -r requirements.txt
```
### Application startup
```bash
uvicorn app.main:app --reload
```
---

## Docker Deployement
## Run it in the project root 
```bash
docker compose up --build
```
---
## Test
### Integration_test
```bash
python -m  pytest ./tests/test_integration.py -v
```
### Conftest
```bash
python -m  pytest ./tests/conf_test.py -v
```
### Secrity Test
```bash
python -m  pytest ./tests/security_test.py -v
```
### Predict Load Test
```bash
python -m tests.predict_load
```

### Batch Predict Load Test
```bash
python -m tests.batch
```
---
## Swagger UI
Swagger UI provides the information about the endpoint thier allowed schemas.
### visit :
 - http://127.0.0.1:8000/docs
 --

## Metrices 
Here,we used the promethuse  monitering system to give help full insights of api endpoints like count,sum of the request and response of the each endpoints
### visit
 - http://127.0.0.0:8000/metrices
 
---

















