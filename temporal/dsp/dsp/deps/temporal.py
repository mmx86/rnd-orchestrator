import typing

import fastapi
import temporalio
import temporalio.client

from .settings import SettingsDep


async def get_temporal_client(
        settings: SettingsDep,
) -> temporalio.client.Client:
    temporal_client = await temporalio.client.Client.connect(
        target_host=settings.TEMPORAL_HOST,
    )
    return temporal_client


TemporalClientDep = typing.Annotated[temporalio.client.Client, fastapi.Depends(get_temporal_client)]
