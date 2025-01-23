import typing

import grpc
import pyzeebe
import fastapi

from .settings import SettingsDep


async def get_grpc_channel(
        settings: SettingsDep,
) -> grpc.aio.Channel:
    channel = pyzeebe.create_insecure_channel(
        grpc_address=settings.ZEEBE_GRPC_ADDRESS,
    )
    return channel


GRPCChannelDep = typing.Annotated[grpc.aio.Channel, fastapi.Depends(get_grpc_channel)]


async def get_zeebe_client(
        grpc_channel: GRPCChannelDep,
) -> pyzeebe.ZeebeClient:
    zeebe_client = pyzeebe.ZeebeClient(grpc_channel=grpc_channel)
    return zeebe_client


ZeebeClientDep = typing.Annotated[pyzeebe.ZeebeClient, fastapi.Depends(get_zeebe_client)]
