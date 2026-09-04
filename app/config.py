from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
        extra="ignore"
    )


    API_V1_STR:str 
    MODEL_PKL_PATH:str
    ACCURACY_PKL_PATH:str


settings=Settings()


