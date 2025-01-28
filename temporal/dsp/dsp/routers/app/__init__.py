import fastapi

from . import workflows


router = fastapi.APIRouter()


router.include_router(workflows.router, prefix='/workflows')
