from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import joblib






class TestData(BaseModel):
    sepallength:float
    sepalwidth:float
    petallength:float
    petalwidth:float


accuracy=joblib.load("ml/saved_model/accuracy.pkl")
pipeline=joblib.load("ml/saved_model/iris_pipeline.pkl")

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
    Y_pred=pipeline.predict(input_data)
    
    result={"result":Y_pred[0],
            "accuracy":accuracy}
    return JSONResponse(content=str(result),status_code=200)
