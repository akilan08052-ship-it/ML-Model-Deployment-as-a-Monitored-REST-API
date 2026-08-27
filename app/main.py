from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.schemas import TestData
import joblib
import gc




ml_model={}
async def lifespan(app:FastAPI):
    model=joblib.load("ml/saved_model/iris_pipeline.pkl")
    print(model)
    ml_model["model"]=model
    print("----model loaded----")
    yield
    print("model released")
    
    del model
    gc.collect()


def convert(data):
    dict_data=f=dict(data)
    return list(dict_data.values())



app=FastAPI(lifespan=lifespan)


@app.get("/")
def root():

    return JSONResponse(content=str({"message":"ML API is live"}),status_code=200)



@app.post("/predict")
def predict(data:TestData):
    con=convert(data)
    result=ml_model["model"].predict([con])
    return JSONResponse(content={"result":str(result[0])},status_code=200)
    
        
    
   