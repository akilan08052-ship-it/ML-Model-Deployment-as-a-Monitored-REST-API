from pydantic import BaseModel,Field
class TestData(BaseModel):
    sepallength:float=Field(ge=0)
    sepalwidth:float=Field(ge=0)
    petallength:float=Field(ge=0)
    petalwidth:float=Field(ge=0)


    
            