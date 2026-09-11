from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from app.routes import v1,v2
from .logging_config import setup
from app.config import settings
import joblib
import gc
import os
import uuid
import datetime
import time


logger=setup()




async def lifespan(app:FastAPI):
    FILE_LOC_MODEL=settings.MODEL_PKL_PATH
    FIEL_LOC_ACCURACY=settings.ACCURACY_PKL_PATH
    try:
        logger.info( "Checking ML model file | path=%s","ml/saved_model/iris_pipeline.pkl")
        if  os.path.exists(FILE_LOC_MODEL):
           model=joblib.load(FILE_LOC_MODEL)
           
           app.state.model=model
           app.state.model_type=type(model).__name__
           
           file_info=os.stat(FILE_LOC_MODEL)
           app.state.model_date=datetime.datetime.fromtimestamp(file_info.st_mtime)
           logger.info("Model.pkl is loaded Successfully")
           
           
        else:
            app.state.model=None
            logger.exception("Model.pkl is not loaded")
            app.state.error=FileNotFoundError("File not in the location:",FILE_LOC_MODEL)
        
        

        if os.path.exists(FIEL_LOC_ACCURACY):
            accuracy=joblib.load(FIEL_LOC_ACCURACY)
            app.state.accuracy=accuracy
            logger.info("accuracy.pkl is loaded Successfully")
            
        else:
            app.state.accuracy=None
            logger.exception("accuracy.pkl not loaded")
            app.state.error=FileNotFoundError("file not fould error in this location:",FIEL_LOC_ACCURACY)
    except Exception as e:
        logger.exception("Unexpected error during startup resource loading")
        raise
    yield
    logger.info("Model is shotdown")
    del model 
    del accuracy
    
    gc.collect()

app=FastAPI(lifespan=lifespan)


@app.middleware("http")
async def rr_handler(request:Request,call_next):
    start_time=time.perf_counter()
    
    request.state.request_id=uuid.uuid4()
    logger.info(
        "Request Recived |"
        "request_id=%s |"
        "method=%s |"
        "path=%s ",
        str(request.state.request_id),
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
                str(request.state.request_id),
                request.method,
                request.url.path,
                duration,
            )
        
    return response

app.include_router(v1.router)
app.include_router(v2.router)
app.add_middleware(
    CORSMiddleware,

        allow_origins=[settings.FRONTEND_URL],
        allow_headers=["*"],
        allow_credentials=True,
        allow_methods=["*"]
        
)




   








    
   

