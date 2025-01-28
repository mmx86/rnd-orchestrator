import enum

import pydantic


class Dataset(pydantic.BaseModel):
    id: int
    branch: str = 'master'


class ModelEvaluation(pydantic.BaseModel):
    score: float


class Inference(pydantic.BaseModel):
    pass


class Interpretation(pydantic.BaseModel):
    pass


class ModelTask(enum.StrEnum):
    CLASSIFICATION = 'CLASSIFICATION'
    CLUSTERISATION = 'CLUSTERIZATION'
    REGRESSION = 'REGRESSION'


class Model(pydantic.BaseModel):
    id: int
    branch: str = 'master'
    task: ModelTask
