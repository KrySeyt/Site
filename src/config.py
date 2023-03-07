from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    postgresql_url: PostgresDsn | None = None

    class Config:
        env_prefix = "SITE_"
        env_nested_delimiter = "__"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
