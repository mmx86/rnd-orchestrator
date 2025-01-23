import asyncio
import random

import pyzeebe

from dsp_worker import models
from dsp_worker.exception_handler import on_error


router = pyzeebe.ZeebeTaskRouter(
    exception_handler=on_error,
)


async def fake_work():
    work_time = random.uniform(1, 1)
    await asyncio.sleep(work_time)


@router.task(task_type='automl-setup-model-task')
async def task_automl_setup_model_task():
    await fake_work()
    model_task = models.ModelTask.CLASSIFICATION
    return {'model_task': model_task}


@router.task(task_type='load-dataset')
async def task_load_dataset(model_task: models.ModelTask):
    await fake_work()
    dataset = models.Dataset()
    return {'dataset': dataset.model_dump(mode='json')}


@router.task(task_type='prepare-dataset')
async def task_prepare_dataset(dataset: models.Dataset):
    await fake_work()
    return {'dataset': dataset}


@router.task(task_type='select-models')
async def task_select_models(model_task: models.ModelTask):
    await fake_work()
    base_models = [models.Model() for _ in range(3)]
    return {'base_models': [m.model_dump(mode='json') for m in base_models]}


@router.task(task_type='train-models')
async def task_train_models(base_models: list[models.Model], dataset: models.Dataset):
    await fake_work()
    trained_models = [models.Model() for m in base_models]
    return {'models': [m.model_dump(mode='json') for m in trained_models]}


@router.task(task_type='evaluate-models')
async def evaluate_models(models: list[models.Model]):
    await fake_work()
    return {'evaluation': {}}


@router.task(task_type='choose-best-model')
async def task_choose_best_model(models: list[models.Model], evaluation: models.Evaluation):
    await fake_work()
    return {'best_model': models[0]}


@router.task(task_type='interpret-model')
async def interpret_model(model: models.Model):
    await fake_work()
    return {'interpretation': True}


@router.task(task_type='push-model')
async def task_push_model(model: models.Model):
    await fake_work()
    return {'model': model}


@router.task(task_type='inference-model')
async def task_inference_model(model: models.Model):
    await fake_work()
    inference = models.Inference()
    return {'inference': inference.model_dump(mode='json')}
