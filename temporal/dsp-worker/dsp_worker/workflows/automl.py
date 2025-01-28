import random

from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError

with workflow.unsafe.imports_passed_through():
    import dsp_worker


@workflow.defn
class AutomlWorkflow:
    @workflow.run
    async def run(self, arg) -> dsp_worker.models.Model:
        rng = random.Random(arg['id'])  # Create a deterministic RNG instance

        retry_policy = RetryPolicy(
            maximum_attempts=3,
            maximum_interval=timedelta(seconds=2),
            non_retryable_error_types=None,  # 4xx
        )

        response = await workflow.execute_activity_method(
            dsp_worker.activities.automl.AutomlActivities.setup_model_task,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy,
        )
        model_task = response['model_task']

        is_dataset_prepared = False
        while not is_dataset_prepared:
            response = await workflow.execute_activity_method(
                dsp_worker.activities.automl.AutomlActivities.load_dataset,
                model_task,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            )
            dataset = response['dataset']

            response = await workflow.execute_activity_method(
                dsp_worker.activities.automl.AutomlActivities.prepare_dataset,
                dataset,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            )
            dataset = response['dataset']

            # value = await workflow.side_effect(lambda: random.random())
            is_dataset_prepared = rng.random() > 0.33

        is_trained_models_check_passed = False
        while not is_trained_models_check_passed:
            response = await workflow.execute_activity_method(
                dsp_worker.activities.automl.AutomlActivities.select_base_models,
                model_task,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            )
            base_models = response['base_models']

            response = await workflow.execute_activity_method(
                dsp_worker.activities.automl.AutomlActivities.train_models,
                base_models,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            )
            trained_models = response['trained_models']

            response = await workflow.execute_activity_method(
                dsp_worker.activities.automl.AutomlActivities.evaluate_models,
                trained_models,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            )
            model_evaluations = response['model_evaluations']

            is_trained_models_check_passed = rng.random() > 0.5

        response = await workflow.execute_activity_method(
            dsp_worker.activities.automl.AutomlActivities.choose_best_model,
            args=[
                base_models,
                model_evaluations,
            ],
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy,
        )
        best_model = response['best_model']

        return best_model
