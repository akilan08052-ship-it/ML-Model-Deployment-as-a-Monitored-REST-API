from fastapi import APIRouter,Request,status
from fastapi.responses import JSONResponse
from app.logging_config import setup
from ..models.schemas import *
from app.config import settings
import pandas as pd

logger=setup()

router=APIRouter(prefix=settings.API_V1_STR)
def convert_df(data):
    input_data = pd.DataFrame( [[ data.sepallength, data.sepalwidth, data.petallength, data.petalwidth ]], 
                            columns=[ "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm" ] )
    
    return input_data






        

@router.get("/")
def root():

    return JSONResponse(content={"message":"ML API is live"},status_code=200)
@router.post("/predict")
def predict(data:PredictionInput,request:Request):
    request_id=request.state.request_id
    model=request.app.state.model
    accuracy=request.app.state.accuracy
    if model is None:
        logger.exception("Prediction attempted but model not loaded | request_id=%s",
            request_id,)
        return JSONResponse(
            content={"request_id": str(request_id), "detail": "Model is not available"},
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )

    
  
    try:
        input_data=convert_df(data)
    except Exception as e:
        logger.exception(
            "Invalid input data | request_id=%s",
            request_id,
        )
        return JSONResponse(
            content={"request_id": str(request_id), "detail": f"Invalid input: {e}"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    try:
        result=model.predict(input_data)
    except Exception as e:
        logger.exception("Model failied | request_id=%s" ,request_id)
        return JSONResponse(content={"request_id":str(request_id),
                                     "details":str(e),},status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    
    return PredictionResponseV1(
        request_id=str(request_id),
        species=str(result[0]),
        accuracy=accuracy
    )

@router.get("/health")
def check_health(request:Request,):
    request_id=str(request.state.request_id)
    model=request.app.state.model
    accuracy_score=request.app.state.accuracy
    if not(model or accuracy_score):
        logger.exception("error during accessing the model varialbles orload model")
        return JSONResponse(content={"request_id":request_id,
                                     "status":" Prediction Service Is Not Available",
                                     "details":"error during accessing the model varialbles"})
    return JSONResponse(content={"request_id":request_id,
                                 "status":"Prediction service is Available"})

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
            prediction=PredictionResponseV1(request_id=request_id,species=str(result),accuracy=accuracy)
            predict_result.append(prediction)
   
    return PredictionBatchOutput(predictions=predict_result)

    

        
    
        

        
           



    
    
   



