import pyzeebe
import loguru


logger = loguru.logger


async def on_error(
        exception: Exception,
        job: pyzeebe.Job,
        job_controller: pyzeebe.JobController,
):
    """
    on_error will be called when the task fails
    """
    logger.error(exception)
    await job_controller.set_error_status(job, f'Failed to handle job {job}. Error: {str(exception)}')


