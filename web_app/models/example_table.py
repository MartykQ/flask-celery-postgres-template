"""
Represents simple table definition
"""

from enum import Enum

from web_app.extensions import db


class ObjectState(Enum):
    """Stores state"""
    STARTED = 0
    FINISHED = 1


class ExampleTable(db.Model):
    """
    Simple db model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    state = db.Column(db.Integer, nullable=True, unique=False)
