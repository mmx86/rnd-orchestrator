# TODO: set default error handler once in router class.
import uuid

import pyzeebe

import dsp_common
import dsp.models

 = lambda (task: pyzeebe.Job): task.

router = pyzeebe.ZeebeTaskRouter(
)


@router.task(task_type='publish-kafka-event', exception_handler=dsp_common.pyzeebe.pyzeebe.on_error)
async def task_publish_kafka_event(name: str) -> dict:
    space = {
        'id': uuid.UUID(),
        'name': name,
    }
    return {'space': space}


@router.task(task_type='insert-db-instance', exception_handler=dsp_common.pyzeebe.pyzeebe.on_error)
async def task_insert_db_instance(space: dsp.models.Space) -> dict:
    return {'output': f'DONE IDI'}


@router.task(task_type='create-authz-data', exception_handler=dsp_common.pyzeebe.pyzeebe.on_error)
async def task_create_authz_data(space: dsp.models.Space) -> dict:
    return {'output': f'DONE CAD'}


@router.task(task_type='create-k8s-namespace', exception_handler=dsp_common.pyzeebe.pyzeebe.on_error)
async def task_create_k8s_namespace(space: dsp.models.Space) -> dict:
    return {'output': f'DONE CKN'}


@router.task(task_type='inject-k8s-agent', exception_handler=dsp_common.pyzeebe.pyzeebe.on_error)
async def task_k8s_agent(name: dsp.models.k8s.K8sNamespace) -> dict:
    return {'output': f'DONE CKN'}
