import asyncio
import coloredlogs
import logging
import uuid

import pyzeebe


coloredlogs.install()
logging.basicConfig(level=logging.DEBUG)


async def on_error(
    exception: Exception,
    job: pyzeebe.Job,
    job_controller: pyzeebe.JobController,
):
    """
    on_error will be called when the task fails
    """
    print(exception)
    await job_controller.set_error_status(job, f'Failed to handle job {job}. Error: {str(exception)}')


async def main():
    channel = pyzeebe.create_insecure_channel(grpc_address='localhost:26500')  # Create grpc channel
    worker = pyzeebe.ZeebeWorker(channel)

    @worker.task(task_type='publish-kafka-event', exception_handler=on_error)
    async def task_publish_kafka_event(name: str) -> dict:
        space = {
            'id': uuid.UUID(),
            'name': name,
        }
        return {'space': space}

    @worker.task(task_type='insert-db-instance', exception_handler=on_error)
    async def task_insert_db_instance(space: models.Space) -> dict:
        return {'output': f'DONE IDI'}

    @worker.task(task_type='create-authz-data', exception_handler=on_error)
    async def task_create_authz_data(space: models.Space) -> dict:
        return {'output': f'DONE CAD'}

    @worker.task(task_type='create-k8s-namespace', exception_handler=on_error)
    async def task_create_k8s_namespace(space: models.Space) -> dict:
        return {'output': f'DONE CKN'}

    @worker.task(task_type='inject-k8s-agent', exception_handler=on_error)
    async def task_k8s_agent(name: models.K8sNamespace) -> dict:
        return {'output': f'DONE CKN'}

    await worker.work()


asyncio.run(main())
