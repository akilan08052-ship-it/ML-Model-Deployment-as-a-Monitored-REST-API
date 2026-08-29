# ML-Model-Deployment-as-a-Monitored-REST-API

  REST API which serve the to predict the the species type of the iris flower using the length and width of sepal,petal of the flower.This Rest API is monitored from request to response for record the purpose of the breakage during the server is running.
-----
## Tech Stack
 - Python
 - FastAPI
 - Uvicorn
 - Pydantic
 - Pandas
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

```text

---

## Used this project 

```bash
git clone "https://github.com/akilan08052-ship-it/ML-Model-Deployment-as-a-Monitored-REST-API.git"

```
### Setup Enviroment
```bash
pip install -r requirement.txt

```
### Run the project

```bash
uvicron app.main:app --reload

```
## Endpoints

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/predict
http://127.0.0.1:8000/health

```


## Response
<img width="1238" height="671" alt="image" src="https://github.com/user-attachments/assets/2613454e-f5ad-465a-9c56-d1519a5038dd" />












