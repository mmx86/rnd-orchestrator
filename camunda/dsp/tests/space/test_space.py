import loguru
import pytest
import pyzeebe

import dsp

logger = loguru.logger


@pytest.mark.asyncio
async def test_create_space(
        zeebe_client: pyzeebe.ZeebeClient,
):
    pass

    ## Run a Zeebe process instance
    #process_instance_key = await zeebe_client.run_process(
    #    bpmn_process_id="Process_1ic93l2",  # "create-space",
    #    variables={},
    #)

    # Run a process and receive the result
    #process_instance_key, process_result = await zeebe_client.run_process_with_result(
    #    bpmn_process_id="Process_1ic93l2",  # "create-space",
    #    timeout=10000,
    #)


    # Cancel a running process
    #await zeebe_client.cancel_process_instance(process_instance_key=12345)


    # Publish message
    #await zeebe_client.publish_message(name="message_name", correlation_key="some_id")
