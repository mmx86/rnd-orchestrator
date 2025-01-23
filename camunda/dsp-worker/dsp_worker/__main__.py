import asyncio

import pyzeebe

from . import routers
from ._settings import settings


async def main():
    # Create GRPC channel.
    channel = pyzeebe.create_insecure_channel(
        grpc_address=settings.ZEEBE_GRPC_ADDRESS,
    )

    # Create zeebe worker.
    worker = pyzeebe.ZeebeWorker(channel)
    worker.include_router(*routers.all_routers)

    # Start zeebe worker.
    await worker.work()


asyncio.run(main())  # https://github.com/camunda-community-hub/pyzeebe/issues/198
