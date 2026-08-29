from pydantic import BaseModel,Field
from fastapi import status
from enum import Enum


class IrisSpecies(Enum):
    IRISSETOSA="iris-setosa"
    ISISVERSICOLOR="iris-versicolor"
    IRISVIRGINICA="iris-virginica"

class InputSpecies(BaseModel):
    sepallength:float=Field(ge=0 ,alias="sepallength")
    sepalwidth:float=Field(ge=0,alias="sepalwidth")
    petallength:float=Field(ge=0,alias="petallength")
    petalwidth:float=Field(ge=0,alias="petalwidth")


class PredictionResponse(BaseModel):
    request_id:str
    species:str
    accuracy:float
    
    
      