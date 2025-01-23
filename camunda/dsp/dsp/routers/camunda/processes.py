import pprint

from loguru import logger
import fastapi

from dsp import deps

router = fastapi.APIRouter()


@router.post('/deploy')
async def deploy(
        zeebe_client: deps.ZeebeClientDep,
        settings: deps.SettingsDep,
):
    resources = []
    for root, dirs, file_names in settings.DSP_PROCESSES_DIR.walk():
        for file_name in file_names:
            file = root / file_name
            resources.append(str(file))

    logger.info(f'Uploading process definitions: \n{pprint.pformat(sorted(resources), width=40)}')
    response = await zeebe_client.deploy_resource(*resources)
    return response
