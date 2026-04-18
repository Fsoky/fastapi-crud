from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

import redis.asyncio as redis

ROOT_DIR = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    POSTGRES_DB: SecretStr
    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: SecretStr
    POSTGRES_PORT: SecretStr
    
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_PASSWORD: SecretStr | None = None
    
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    
    @property
    def db_url(self) -> str:
        return (
            "asyncpg://"
            f"{self.POSTGRES_USER.get_secret_value()}:{self.POSTGRES_PASSWORD.get_secret_value()}"
            f"@{self.POSTGRES_HOST.get_secret_value()}:{self.POSTGRES_PORT.get_secret_value()}"
            f"/{self.POSTGRES_DB.get_secret_value()}"
        )
    
    @property
    def redis_pwd(self) -> str | None:
        return self.REDIS_PASSWORD.get_secret_value() if self.REDIS_PASSWORD else None

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8"
    )


config = Config() # type: ignore

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.redis_pwd,
    decode_responses=True
)

TORTOISE_ORM = {
    "connections": {"default": config.db_url},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}