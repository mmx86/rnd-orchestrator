import fastapi

from dsp import deps


router = fastapi.APIRouter()


@router.post('/')
async def create_automl_process(
        zeebe_client: deps.ZeebeClientDep,
):
    # Run a Zeebe process instance.
    response = await zeebe_client.run_process(
        bpmn_process_id='dsp-create-space',
        variables={},
    )
    return response
