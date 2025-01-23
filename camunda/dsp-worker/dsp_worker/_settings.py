import pprint

from loguru import logger

import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    ZEEBE_GRPC_ADDRESS: str


settings: Settings = Settings()
logger.info(pprint.pformat(settings.model_dump()))
