import dataclasses
import pathlib
import pprint

import grpc
import loguru
import pytest
import pyzeebe

import dsp


logger = loguru.logger


@pytest.fixture
async def grpc_channel() -> grpc.aio.Channel:
    channel = pyzeebe.create_insecure_channel(
        grpc_address=dsp.settings.ZEEBE_GRPC_ADDRESS,
    )
    return channel


@pytest.fixture
async def zeebe_client(
        grpc_channel,
) -> pyzeebe.ZeebeClient:
    zeebe_client = pyzeebe.ZeebeClient(grpc_channel=grpc_channel)
    return zeebe_client


@pytest.fixture
async def deploy_processes(
        zeebe_client: pyzeebe.ZeebeClient,
):
    processes_dir = pathlib.Path('dsp/processes/')

    resources = []
    for root, dirs, file_names in processes_dir.walk():
        for file_name in file_names:
            file = root / file_name
            resources.append(str(file))

    logger.info(
        f'Uploading resources in "{processes_dir}": '
        f'{pprint.pformat(resources)}'
    )
    response = await zeebe_client.deploy_resource(*resources)
    logger.info('Response:\n' + pprint.pformat(dataclasses.asdict(response)))
