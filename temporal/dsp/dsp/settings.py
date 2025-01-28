import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    TEMPORAL_HOST: str  # host:port
