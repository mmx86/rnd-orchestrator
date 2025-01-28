import sys

import loguru

loguru.logger.configure(
    handlers=[
        {'sink': sys.stderr, 'level': 'DEBUG'},
    ],
)
