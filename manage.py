"""
CLI commands and utilities
"""

from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from web_app import create_app
from web_app.extensions import db

app = create_app()
cli = FlaskGroup(create_app=create_app)

manager = Manager(app)
migrate = Migrate(app, db)

# adds the python manage.py db init, db migrate, db upgrade commands
manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    """Run flask application"""
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def recreate_db():
    """
    Recreates a database. This should only be used once
    when there's a new database instance. This shouldn't be
    used when you migrate your database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
