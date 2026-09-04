from fastapi import APIRouter,Response,Request,status,FastAPI
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from app.logging_config import setup
from ..models.schemas import *
from app.config import settings
import pandas as pd
import joblib
import uuid
import time
import datetime 
import os
import gc
logger=setup()

router=APIRouter(prefix=settings.API_V1_STR)
def convert_df(data):
    input_data = pd.DataFrame( [[ data.sepallength, data.sepalwidth, data.petallength, data.petalwidth ]], 
                            columns=[ "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm" ] )
    
    return input_data






        

@router.get("/")
def root():

    return JSONResponse(content=str({"message":"ML API is live"}),status_code=200)
@router.post("/predict")
def predict(data:PredictionInput,request:Request):
    request_id=request.state.request_id
  
    try:
        input_data=convert_df(data)
        result=getattr(request.app.state,"model").predict(input_data)
        accuracy=getattr(request.app.state,"accuracy")
    except Exception as e:
        logger.exception(
            "Prediction error |"
            "request_id=%s"
            "error=%s",
            request_id,
            str(e)
        )
        return JSONResponse(content=str(getattr(request.app.state,"error")),status_code=status.HTTP_404_NOT_FOUND)
    
    return PredictionResponse(
        request_id=str(request_id),
        species=str(result[0]),
        accuracy=accuracy
    )

@router.get("/health")
def check_health(request:Request,):
    
    model_loaded=getattr(request.app.state,"model")
    accuracy_loaded=getattr(request.app.state,"accuracy")
    if model_loaded and accuracy_loaded:
        model_status="Prediction  service is Avaialble"
        return JSONResponse(content={"status":model_status},status_code=status.HTTP_200_OK)
    else:
        model_status="Prediction service is not  Avaialble"
        logger.warning("PKL file is not active |" "method=%s|" "path=%s|",request.method,request.url.path)
        return JSONResponse(content={"status":model_status},status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
model_data={}
@router.get("/model-info")
def model_info(request:Request):
    model=getattr(request.app.state,"model")
    model_type=str(model.steps[1][1])
    trained_date=str(getattr(request.app.state,"model_date").date())
 
    return MoelInfo(model_type=model_type,trained_date=trained_date)

@router.post("/batch-prediction")
def batch_predict(data:PredictionBatchInput,request:Request):
    request_id=str(request.state.request_id)
    accuracy=getattr(request.app.state,"accuracy")
    model=getattr(request.app.state,"model")
    predict_result=[]

    input=data.inputs
    
    for items in input:
        df=pd.DataFrame( [[ items.sepallength, items.sepalwidth, items.petallength, items.petalwidth ]], 
                            columns=[ "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm" ] )
        predictions=model.predict(df)
        for result in predictions:
            prediction=PredictionResponse(request_id=request_id,species=str(result),accuracy=accuracy)
            predict_result.append(prediction)
   
    return PredictionBatchOutput(predictions=predict_result)

    

        
    
        

        
           



    
    
   



