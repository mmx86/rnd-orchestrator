import asyncio
import dataclasses
import pprint

import loguru
import pyzeebe

import dsp

logger = loguru.logger


async def main():
    # Create a zeebe client
    channel = pyzeebe.create_insecure_channel(grpc_address=dsp.settings.ZEEBE_GRPC_ADDRESS)
    zeebe_client = pyzeebe.ZeebeClient(channel)

    # Deploy a BPMN process definition
    response = await zeebe_client.deploy_resource("dsp/processes/create-space.bpmn")
    logger.info('Response:\n' + pprint.pformat(dataclasses.asdict(response)))

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


asyncio.run(main())
