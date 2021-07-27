"""Helper script to make sure celery worker is started correctly"""

from web_app.extensions import FlaskCelery
from web_app import create_app
app = create_app()
celery = FlaskCelery(app=app)
