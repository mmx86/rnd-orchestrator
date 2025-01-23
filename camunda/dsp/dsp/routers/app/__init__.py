import fastapi

from . import processes


router = fastapi.APIRouter()


router.include_router(processes.router, prefix='/processes')
