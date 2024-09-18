from typing import Optional
from pydantic_settings import BaseSettings

class DBEnv(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    class Config:
        env_file = ".env"

db_env = DBEnv()