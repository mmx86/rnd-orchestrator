import pathlib

import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    DSP_BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent
    DSP_PROCESSES_DIR: pathlib.Path = DSP_BASE_DIR / 'processes'

    ZEEBE_GRPC_ADDRESS: str
