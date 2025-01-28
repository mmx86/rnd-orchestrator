import fastapi

from . import app


router = fastapi.APIRouter()


router.include_router(app.router, prefix='/app/v1')
