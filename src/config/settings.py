from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: str
    admin_id: str | None = "6288131392 501796953"
    users_db: str | None = "users"
    info_db: str | None = "static"
    diagram: str = "diagram.png"

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
