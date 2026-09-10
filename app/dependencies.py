from fastapi import Header,HTTPException,status

from app.config import settings



def verify_api_key(x_api_key:str | None=Header(default=None)):
    if x_api_key==None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="api key is required ")
    if x_api_key!=settings.API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="api key is invalid")
    return x_api_key
