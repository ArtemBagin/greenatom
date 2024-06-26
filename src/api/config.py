from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path("../../.env"), env_file_encoding='utf-8')

    robot_file_name: str = 'bot.py'
    robot_path: str = '../robot/bot.py'
    database: str


settings = Settings()
