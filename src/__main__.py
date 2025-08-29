from typing import AsyncGenerator

from fastapi import FastAPI
import uvicorn

from tortoise import Tortoise

from api import setup_routers
from config_reader import config, TORTOISE_ORM


async def lifespan(app: FastAPI) -> AsyncGenerator:
    await Tortoise.init(TORTOISE_ORM)
    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)
app.include_router(setup_routers())


if __name__ == "__main__":
    uvicorn.run("__main__:app", host=config.APP_HOST, port=config.APP_PORT, reload=True)