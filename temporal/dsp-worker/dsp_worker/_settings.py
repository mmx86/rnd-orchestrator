import pprint

from loguru import logger

import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    TEMPORAL_HOST: str  # host:port


settings: Settings = Settings()
logger.info(pprint.pformat(settings.model_dump()))
