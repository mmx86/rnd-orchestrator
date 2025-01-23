import fastapi

from . import app
from . import camunda


router = fastapi.APIRouter()


router.include_router(app.router, prefix='/app/v1')
router.include_router(camunda.router, prefix='/camunda')
