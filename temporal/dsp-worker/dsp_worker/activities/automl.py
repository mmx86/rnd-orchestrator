import asyncio
import random
import typing

from temporalio import activity

import dsp_worker


async def fake_work(
        t_mix: int = 1,
        t_max: int = 4,
):
    work_time = random.uniform(t_mix, t_max)
    await asyncio.sleep(work_time)


class AutomlActivities:
    @activity.defn
    async def setup_model_task(
            self,
    ) -> typing.TypedDict('SetupModelTaskOut', {'model_task': dsp_worker.models.ModelTask}):
        activity.logger.info('Running setup_model_task')
        model_task = dsp_worker.models.ModelTask.CLASSIFICATION
        await fake_work()
        return {'model_task': model_task}

    @activity.defn
    async def load_dataset(
            self,
            model_task: dsp_worker.models.ModelTask,
    ) -> typing.TypedDict('LoadDatasetOut', {'dataset': dsp_worker.models.Dataset}):
        activity.logger.info('Running load_dataset')
        dataset = dsp_worker.models.Dataset(id=1, branch='master')
        await fake_work()
        return {'dataset': dataset}

    @activity.defn
    async def prepare_dataset(
            self,
            dataset: dsp_worker.models.Dataset,
    ) -> typing.TypedDict('LoadDatasetOut', {'dataset': dsp_worker.models.Dataset}):
        activity.logger.info('Running prepare_dataset')
        dataset = dsp_worker.models.Dataset(id=1, branch='prepared')
        await fake_work()
        return {'dataset': dataset}

    @activity.defn
    async def select_base_models(
            self,
            model_task: dsp_worker.models.ModelTask,
    ) -> typing.TypedDict('SelectBaseModelOut', {'base_models': list[dsp_worker.models.Model]}):
        activity.logger.info('Running select_base_models')
        base_models = [
            dsp_worker.models.Model(id=1, branch='master', task=model_task),
            dsp_worker.models.Model(id=2, branch='develop', task=model_task),
        ]
        await fake_work()
        return {'base_models': base_models}

    @activity.defn
    async def train_models(
            self,
            base_models: list[dsp_worker.models.Model],
    ) -> typing.TypedDict('TrainModelOut', {'trained_models': list[dsp_worker.models.Model]}):
        activity.logger.info('Running train_models')
        for m in base_models:
            m.branch = f'{m.branch}/fine-tuned'
        trained_models = base_models
        await fake_work()
        return {'trained_models': trained_models}

    @activity.defn
    async def evaluate_models(
            self,
            trained_models: list[dsp_worker.models.Model],
    ) -> typing.TypedDict('EvaluateModelsOut', {'model_evaluations': list[dsp_worker.models.ModelEvaluation]}):
        activity.logger.info('Running evaluate_models')
        model_evaluations = [
            dsp_worker.models.ModelEvaluation(score=random.random())
            for _ in trained_models
        ]
        await fake_work()
        return {'model_evaluations': model_evaluations}

    @activity.defn
    async def choose_best_model(
            self,
            trained_models: list[dsp_worker.models.Model],
            model_evaluations: list[dsp_worker.models.ModelEvaluation],
    ) -> typing.TypedDict('ChooseBestModelOut', {'best_model': dsp_worker.models.Model}):
        activity.logger.info('Running choose_best_model')
        max_score = -1
        best_model = None
        for model, model_evaluation in zip(trained_models, model_evaluations):
            if model_evaluation.score > max_score:
                best_model = model
        if best_model is None:
            raise ValueError('Best model cannot be None')
        await fake_work()
        return {'best_model': best_model}
