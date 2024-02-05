from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv

conf_file = find_dotenv()


class DbConfig(BaseSettings):
    DB_URL: str

    model_config = SettingsConfigDict(env_file=conf_file)


db_config = DbConfig()
