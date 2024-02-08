from pydantic_settings import BaseSettings, SettingsConfigDict
from src.app_config import env_file


class DbConfig(BaseSettings):
    DB_URL: str
    # BD_ECHO: bool = False
    BD_ECHO: bool = True

    model_config = SettingsConfigDict(env_file=env_file, extra="ignore")


db_config = DbConfig()
