import uuid

import fastapi

from dsp import deps


router = fastapi.APIRouter()

AUTOML_TASK_QUEUE = 'AUTOML_TASK_QUEUE'  # TODO: move to shared


@router.post('/run')
async def run(
        temporal_client: deps.TemporalClientDep,
):
    workflow_id = uuid.uuid4()
    arg = {
        'id': workflow_id,
    }
    response = await temporal_client.execute_workflow(
        'AutomlWorkflow',
        arg,
        id=f'user-process-{workflow_id}',
        task_queue=AUTOML_TASK_QUEUE,
    )

    return response
