"""
Periodic task for handling TriageIssues state
"""

import logging


# from web_app.extensions import db


def example_scheduled_task():
    """
    Iterates over issues stored in TriageIssue table and checks if it needs an update.
    """
    logging.info("Scheduled task started")
