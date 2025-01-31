import uuid

import pyzeebe

from dsp_worker import models
from dsp_worker.exception_handler import on_error

# = lambda (task: pyzeebe.Job): task.


router = pyzeebe.ZeebeTaskRouter(
    exception_handler=on_error,
)


@router.task(task_type='publish-kafka-event')
async def task_publish_kafka_event(name: str) -> dict:
    space = models.Space(
        id=uuid.uuid4(),
        name=name,
    )
    return {'space': space.model_dump(mode='json')}


@router.task(task_type='create-db-instance')
async def task_create_db_instance(space: models.Space) -> dict:
    return {'output': f'DONE CDI'}


@router.task(task_type='create-authz-data')
async def task_create_authz_data(space: models.Space) -> dict:
    return {'output': f'DONE CAD'}


@router.task(task_type='create-k8s-namespace')
async def task_create_k8s_namespace(space: models.Space) -> dict:
    k8s_namespace = models.k8s.Namespace(
        name=space.name,
    )
    return {'k8s_namespace': k8s_namespace.model_dump(mode='json')}


@router.task(task_type='create-k8s-agent')
async def task_create_k8s_agent(k8s_namespace: models.k8s.Namespace) -> dict:
    return {'output': f'DONE CKA'}
