from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

import redis.asyncio as redis

ROOT_DIR = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    DB_URL: SecretStr
    
    APP_HOST: str = "localhost"
    APP_PORT: int = 8080

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8"
    )


class RedisConfig(BaseSettings):
    HOST: str
    PORT: int
    PASSWORD: SecretStr | None = None
    
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env.redis",
        env_file_encoding="utf-8"
    )
    
    def get_password(self) -> str | None:
        return self.PASSWORD.get_secret_value() if self.PASSWORD else None


config = Config() # type: ignore
redis_config = RedisConfig() # type: ignore

redis_client = redis.Redis(
    host=redis_config.HOST,
    port=redis_config.PORT,
    password=redis_config.get_password(),
    decode_responses=True
)

TORTOISE_ORM = {
    "connections": {"default": config.DB_URL.get_secret_value()},
    "apps": {
        "models": {
            "models": [
                "src.db.models.user",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}