import enum

import pydantic


class Dataset(pydantic.BaseModel):
    pass


class Evaluation(pydantic.BaseModel):
    pass


class Inference(pydantic.BaseModel):
    pass


class Interpretation(pydantic.BaseModel):
    pass


class Model(pydantic.BaseModel):
    pass


class ModelTask(enum.StrEnum):
    CLASSIFICATION = 'CLASSIFICATION'
    CLUSTERISATION = 'CLUSTERIZATION'
    REGRESSION = 'REGRESSION'
