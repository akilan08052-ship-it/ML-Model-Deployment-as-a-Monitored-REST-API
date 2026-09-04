from pydantic import BaseModel,Field
from fastapi import status
from typing import List
from enum import Enum
from datetime import datetime


class IrisSpecies(Enum):
    IRISSETOSA="iris-setosa"
    ISISVERSICOLOR="iris-versicolor"
    IRISVIRGINICA="iris-virginica"

class PredictionInput(BaseModel):
    sepallength:float=Field(ge=0 ,alias="sepallength")
    sepalwidth:float=Field(ge=0,alias="sepalwidth")
    petallength:float=Field(ge=0,alias="petallength")
    petalwidth:float=Field(ge=0,alias="petalwidth")



class PredictionResponse(BaseModel):
    request_id:str
    species:str
    accuracy:float

class MoelInfo(BaseModel):
    model_type:str
    trained_date:str
    

class PredictionBatchInput(BaseModel):
    inputs:List[PredictionInput]=Field(min_length=1,max_length=100)

class PredictionBatchOutput(BaseModel):
    predictions:list[PredictionResponse]
    
    
      