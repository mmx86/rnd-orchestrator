import fastapi

from . import automl


router = fastapi.APIRouter()


router.include_router(automl.router, prefix='/automl')
