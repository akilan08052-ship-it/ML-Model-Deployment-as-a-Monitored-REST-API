from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import pickle
import os





class TestData(BaseModel):
    sepallength:float
    sepalwidth:float
    petallength:float
    petalwidth:float

model=joblib.load("ml/saved_model/model.pkl")
scaler=joblib.load("ml/saved_model/scaler.pkl")
accuracy=joblib.load("ml/saved_model/accuracy.pkl")










app=FastAPI()

@app.get("/")
def root():
    return {"message":"ML API is alive"}

@app.post("/predict")
def predict(data: TestData):
    
    input_data = [[
                data.sepallength,
                data.sepalwidth,
                data.petallength,
                data.petalwidth
                ]]
    transformed_data=scaler.transform(input_data)
    result=model.predict(transformed_data)

    return {"reslut":result[0],
            "accuracy":accuracy}