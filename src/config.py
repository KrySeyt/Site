from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn | None = None


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
