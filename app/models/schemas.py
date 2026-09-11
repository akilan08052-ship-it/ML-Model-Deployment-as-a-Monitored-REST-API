from pydantic import BaseModel,Field
from pydantic.config import ConfigDict
from typing import List
from enum import Enum



class IrisSpecies(Enum):
    IRISSETOSA="iris-setosa"
    ISISVERSICOLOR="iris-versicolor"
    IRISVIRGINICA="iris-virginica"

class PredictionInput(BaseModel):
    model_config=ConfigDict(extra="forbid")
    sepallength:float=Field(ge=0 ,alias="sepallength")
    sepalwidth:float=Field(ge=0,alias="sepalwidth")
    petallength:float=Field(ge=0,alias="petallength")
    petalwidth:float=Field(ge=0,alias="petalwidth")

class PredictionResponseV1(BaseModel):
    request_id:str
    species:str
    accuracy:float

class PredictionResponseV2(BaseModel):
    request_id:str
    species:str
    accuracy:float
    model_type:str
    
class PredictionBatchInput(BaseModel):
    inputs:List[PredictionInput]=Field(min_length=1,max_length=100)

class PredictionBatchOutput(BaseModel):
    predictions:list[PredictionResponseV1]
 
class MoelInfo(BaseModel):
    model_type:str
    trained_date:str
      