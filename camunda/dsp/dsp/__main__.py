import asyncio

import pyzeebe

from . import routers
from . import settings


async def main():
    # Build zeebe worker.
    channel = pyzeebe.create_insecure_channel(grpc_address=settings.ZEEBE_GRPC_ADDRESS)  # Create grpc channel
    worker = pyzeebe.ZeebeWorker(channel)
    worker.include_router(*routers.all_routers)

    # Start worker.
    await worker.work()


asyncio.run(main())  # https://github.com/camunda-community-hub/pyzeebe/issues/198
