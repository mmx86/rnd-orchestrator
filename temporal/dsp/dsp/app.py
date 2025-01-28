import fastapi

from . import routers


app = fastapi.FastAPI(
    title='DSP API',
)

app.include_router(routers.router)
