import fastapi

from dsp import deps


router = fastapi.APIRouter()


@router.post('/')
async def create_automl_process(
        zeebe_client: deps.ZeebeClientDep,
):
    # Run a Zeebe process instance.
    response = await zeebe_client.run_process(
        bpmn_process_id='dsp-create-automl-process',
        variables={},
    )

    # Run a process and receive the result.
    # process_instance_key, process_result = await zeebe_client.run_process_with_result(
    #     bpmn_process_id='dsp-create-automl-process',
    #     timeout=10000,
    # )

    # Cancel a running process.
    # await zeebe_client.cancel_process_instance(process_instance_key=process_instance_key)

    # Publish message.
    # await zeebe_client.publish_message(name='message_name', correlation_key='some_id')

    return response
