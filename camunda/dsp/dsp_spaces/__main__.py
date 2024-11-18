import asyncio
import coloredlogs
import logging

import pyzeebe

import dsp.routers


# Logs.
coloredlogs.install()
logging.basicConfig(level=logging.DEBUG)


async def main():
    # Zeebe worker and routers.
    channel = pyzeebe.create_insecure_channel(grpc_address='localhost:26500')  # Create grpc channel
    worker = pyzeebe.ZeebeWorker(channel)
    worker.include_router(
        dsp.routers.create_space_router,
    )
    await worker.work()


# NOTE: https://github.com/camunda-community-hub/pyzeebe/issues/198
asyncio.run(main())
