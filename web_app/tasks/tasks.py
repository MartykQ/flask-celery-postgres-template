"""
Definitions of tasks executed by Celery
"""

import logging

from web_app.extensions import celery
from web_app.extensions import db
from web_app.models.example_table import ExampleTable
from web_app.scheduled_tasks.scheduled_task import example_scheduled_task


@celery.task(name="healthcheck_task")
def healthcheck_task():
    """Healthcheck task"""
    i = db.session.query(ExampleTable)
    logging.info(i)


@celery.task(name='example_task_scheduled')
def example_task_scheduled():
    """Periodic task to update TriageIssue state"""
    logging.info('Update triage issues invoked')
    example_scheduled_task()


@celery.task(name='make_sure_cron_works')
def test_task():
    """Helper task to make sure than scheduled tasks work as expected"""
    logging.debug('Cron works as expected')
