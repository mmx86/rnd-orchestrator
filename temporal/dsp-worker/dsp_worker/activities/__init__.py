"""
An Activity is a method that encapsulates business logic prone to failure (e.g., calling a service that may go down).
These Activities can be automatically retried upon some failure.
"""
from . import automl


automl_activities = automl.AutomlActivities()  # bad


ALL_ACTIVITIES = [
    automl_activities.choose_best_model,
    automl_activities.evaluate_models,
    automl_activities.load_dataset,
    automl_activities.prepare_dataset,
    automl_activities.select_base_models,
    automl_activities.setup_model_task,
    automl_activities.train_models,
]
