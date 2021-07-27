"""
Schedule for tasks that need to be run periodically
"""

from celery.schedules import crontab

TASK_SCHEDULE = {
    # Runs every full hour
    'update-triage-issues': {
        'task': 'example_task_scheduled',
        'schedule': crontab(minute=0, hour='*/1')
    },
    # Runs every 10 minutes
    'make-sure-cron-works': {
        'task': 'make_sure_cron_works',
        'schedule': crontab(minute='*/3')
    }
}
