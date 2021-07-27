"""
main module
"""

import logging
import os

import redis
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from web_app.common.settings import DATA_FMT, LOGGING_FILE, LOGGING_FORMAT, Develop, Prod
from web_app.extensions import celery, db
from web_app.routes.basic_routes import basic_routes

__mode = os.environ.get('MODE') or 'Development'

logging.basicConfig(filename=LOGGING_FILE,
                    filemode='a',
                    format=LOGGING_FORMAT,
                    level=logging.DEBUG,
                    datefmt=DATA_FMT)

REDIS_CLIENT = redis.Redis(host='redis', port='6379')


def create_app():
    """Creates Flask instance"""
    app = Flask(__name__)
    CORS(app)
    mode = os.environ.get('MODE') or 'Develop'
    if mode == 'Develop':
        settings_obj = Develop
    else:
        settings_obj = Prod

    app.config.from_object(settings_obj)
    logging.info(f"Starting flask in {mode} mode ...")

    db.init_app(app)
    Migrate(app, db)
    celery.init_app(app)

    app.register_blueprint(basic_routes)

    return app
