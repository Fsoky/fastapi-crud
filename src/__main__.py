from typing import AsyncGenerator, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from tortoise import Tortoise

from src.api import setup_routers
from src.core.config import config, TORTOISE_ORM


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    await Tortoise.init(TORTOISE_ORM)
    
    # Fix terminal freeze bug
    try:
        yield
    finally:
        await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)
app.include_router(setup_routers())


if __name__ == "__main__":
    uvicorn.run("src.__main__:app", host=config.APP_HOST, port=config.APP_PORT, reload=True)