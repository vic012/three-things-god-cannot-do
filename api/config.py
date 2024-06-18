from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	token_api: str

	model_config = SettingsConfigDict(env_file=".env")

	DATABASE_URL: str

@lru_cache
def get_settings():
	return Settings()
