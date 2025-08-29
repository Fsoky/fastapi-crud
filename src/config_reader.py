from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    DB_URL: SecretStr
    
    APP_HOST: str = "localhost"
    APP_PORT: int = 8080

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / "src" / ".env",
        env_file_encoding="utf-8"
    )


config = Config()

TORTOISE_ORM = {
    "connections": {"default": config.DB_URL.get_secret_value()},
    "apps": {
        "models": {
            "models": [
                "db.models.user",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}