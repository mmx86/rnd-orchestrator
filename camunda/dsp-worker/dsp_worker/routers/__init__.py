from .spaces import create_space
from .processes import automl


all_routers = [
    automl.router,
    create_space.router,
]
