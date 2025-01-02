import sys

import loguru

from ._settings import settings


loguru.logger.configure(
    handlers=[
        {'sink': sys.stderr, 'level': 'DEBUG'},
    ],
)
