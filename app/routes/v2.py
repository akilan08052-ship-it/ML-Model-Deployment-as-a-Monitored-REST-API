from fastapi import APIRouter,Request,status
from fastapi_versionizer.versionizer import api_version
from fastapi.responses import JSONResponse
from app.logging_config import setup
from ..models.schemas import *
from app.config import settings
import pandas as pd





router=APIRouter(prefix=settings.API_V2_STR)
def convert_df(data):
    input_data = pd.DataFrame( [[ data.sepallength, data.sepalwidth, data.petallength, data.petalwidth ]], 
                            columns=[ "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm" ] )
    
    return input_data

@router.post("/predict",status_code=status.HTTP_200_OK)
def predict(data:PredictionInput,request:Request):
    input_data=convert_df(data)
    request_id=str(request.state.request_id)
    model=request.app.state.model
    model_type=str(model.steps[1][1])
    result=model.predict(input_data)
    accuracy=request.app.state.accuracy

    return PredictionResponseV2(request_id=request_id,species=result[0],accuracy=accuracy,model_type=model_type)
