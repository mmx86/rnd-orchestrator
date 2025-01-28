import asyncio
import temporalio.client
import temporalio.worker

from ._settings import settings

import dsp_worker


AUTOML_TASK_QUEUE= 'AUTOML_TASK_QUEUE'


async def main():
    # Create temporal client.
    client = await temporalio.client.Client.connect(
        namespace='default',
        target_host=settings.TEMPORAL_HOST,
    )

    # Create temporal worker.
    worker = temporalio.worker.Worker(
        client,
        task_queue=AUTOML_TASK_QUEUE,
        workflows=dsp_worker.workflows.ALL_WORKFLOWS,
        activities=dsp_worker.activities.ALL_ACTIVITIES,
    )

    # Start temporal worker
    await worker.run()


asyncio.run(main())
