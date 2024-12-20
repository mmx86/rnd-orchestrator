import pydantic


class K8sNamespace(pydantic.BaseModel):
    name: str
