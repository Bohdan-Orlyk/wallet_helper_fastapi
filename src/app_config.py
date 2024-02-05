from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv

env_file = find_dotenv()


class AppConfig(BaseSettings):
    PORT: int
    HOST: str

    model_config = SettingsConfigDict(env_file=env_file, extra="ignore")


app_config = AppConfig()
