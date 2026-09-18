# ML-Model-Deployment-as-a-Monitored-REST-API

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

## project structure

```text
ML-Model-Deployment-as-a-Mointered-REST Api
|
|_app
| |__logs
|   |_app.log
|
|
|_models
|
|_routes
|
|_ml
| |-saved_model
| |   |_model.pkl
| |   |_accuracy.pkl
| |   |_scaler.pkl
| |_iris.csv
| |_train.py
|
|
|
|_test
|
|
|
|_.gitignore
|
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















