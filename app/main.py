from fastapi import FastAPI,Response,Request
from fastapi import status
from fastapi.responses import JSONResponse
from .models.schemas import InputSpecies,PredictionResponse
from logging.handlers import RotatingFileHandler
from .logging_config import setup
import pandas as pd
import joblib
import gc
import os
import uuid
import time


logger=setup()

model_data={}
#--------------------
#startup
#--------------------

async def lifespan(app:FastAPI):
    FILE_LOC_MODEL="ml/saved_model/iris_pipeline.pkl"
    FIEL_LOC_ACCURACY="ml/saved_odel/accuracy.pkl"
    try:
        logger.info( "Checking ML model file | path=%s","ml/saved_model/iris_pipeline.pkl")
        if  os.path.exists(FILE_LOC_MODEL):
           model=joblib.load(FILE_LOC_MODEL)
           model_data["model"]=model
           app.state.model=model
           logger.info("Model.pkl is loaded Successfully")
           
           
        else:
            app.state.model=None
            logger.warning("Model.pkl is not loaded")
            
            model_data["model_error"]=FileNotFoundError("File not in the location:",FILE_LOC_MODEL)
        
        

        if os.path.exists(FIEL_LOC_ACCURACY):
            accuracy=joblib.load(FIEL_LOC_ACCURACY)
            model_data["accuracy"]=accuracy
            app.state.accuracy=accuracy
            logger.info("accuracy.pkl is loaded Successfully")
            
        else:
            app.state.accuracy=None
            logger.warning("accuracy.pkl not loaded")
            model_data["model_error"]=FileNotFoundError("file not fould error in this location:",FIEL_LOC_ACCURACY)
    except Exception as e:
        raise FileNotFoundError(e)
    yield
    logger.info("Model is shotdown")
    del model 
    del accuracy
    
    gc.collect()

#---------------------
#extract the values from request
#---------------------
def convert_df(data):
    input_data = pd.DataFrame( [[ data.sepallength, data.sepalwidth, data.petallength, data.petalwidth ]], 
                            columns=[ "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm" ] )
    
    return input_data

#--------------------
#app
#--------------------
app=FastAPI(lifespan=lifespan)

@app.middleware("http")
async def rr_handler(request:Request,call_next):
    start_time=time.perf_counter()
    request_id=uuid.uuid4()
    request.state.request_id=request_id
    logger.info(
        "Request Recived |"
        "request_id=%s |"
        "method=%s |"
        "path=%s ",
        request_id,
        request.method,
        request.url.path

    )
    

    response=await call_next(request)

    duration=time.perf_counter()-start_time 


    logger.info(
            "Response Sent |"
            "request_id=%s |"
            "request_method=%s |"
            "path=%s |"
            "response_time=%s ",
            str(request_id),
            request.method,
            request.url.path,
            duration,
        )
    
    return response
    
   
    


    

#-------------------
#Endpoints
#-------------------
@app.get("/")
def root():

    return JSONResponse(content=str({"message":"ML API is live"}),status_code=200)


#-------------------
#prediction endpoint
#-------------------
@app.post("/predict",status_code=status.HTTP_200_OK)
def predict(data:InputSpecies,request:Request):
    request_id=request.state.request_id
  
    try:
        input_data=convert_df(data)
        result=model_data["model"].predict(input_data)
        accuracy=model_data["accuracy"]
    except Exception as e:
        logger.exception(
            "Prediction erro |"
            "request_id=%s"
            "error=%s",
            request_id,
            str(e)
        )
        return JSONResponse(content=str(model_data["model_error"]),status_code=status.HTTP_404_NOT_FOUND)
    
    return PredictionResponse(
        request_id=str(request_id),
        species=str(result[0]),
        accuracy=accuracy
    )

#-------------------
#health endpoint
#-------------------
@app.get("/health")
def check_health(request:Request):
    
    model_loaded=getattr(app.state,"model")
    accuracy_loaded=getattr(app.state,"accuracy")
    if model_loaded and accuracy_loaded:
        model_status="Prediction  service is Avaialble"
        return JSONResponse(content={"status":model_status},status_code=status.HTTP_200_OK)
    else:
        model_status="Prediction service is not  Avaialble"
        logger.warning("PKL file is not active |" "method=%s|" "path=%s|",request.method,request.url.path)
        return JSONResponse(content={"status":model_status},status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    
   

