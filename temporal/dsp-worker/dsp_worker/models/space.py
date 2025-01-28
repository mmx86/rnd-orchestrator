import uuid

import pydantic


class Space(pydantic.BaseModel):
    id: uuid.UUID
    name: str