"""
This resolves the issue of celery and flask instances having access to the same db object
"""
# pylint: disable-all
import flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from web_app.scheduled_tasks import TASK_SCHEDULE


class FlaskCelery(Celery):
    """Celery class wrapper to make it work with flask instance"""

    def __init__(self, *args, **kwargs):

        super(FlaskCelery, self).__init__(*args, **kwargs)
        self.patch_task()

        if 'app' in kwargs:
            self.init_app(kwargs['app'])

    def patch_task(self):
        TaskBase = self.Task
        _celery = self

        class ContextTask(TaskBase):
            """Adds flask context to the celery task"""
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
                else:
                    with _celery.app.app_context():
                        return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        self.app = app
        self.autodiscover_tasks(packages=['web_app.tasks'])
        self.conf.beat_schedule = TASK_SCHEDULE

        self.config_from_object(CelConfig)


class CelConfig:
    broker_url = "redis://redis:6379"
    celery_result_backend = "redis://redis:6379"
    broker = "redis://redis:6379"
    backend = "redis://redis:6379"


celery = FlaskCelery()
db = SQLAlchemy()
