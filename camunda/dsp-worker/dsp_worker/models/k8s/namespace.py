import pydantic


class Namespace(pydantic.BaseModel):
    name: str
