import sys

from loguru import logger

from ._settings import settings


logger.configure(
    handlers=[
        {'sink': sys.stderr, 'level': 'DEBUG'},
    ],
)
