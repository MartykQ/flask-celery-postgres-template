# flask-celery-postgres-template (dockerized)

This is an example python flask web app with a Celery tasks, redis broker and Postgres database.

Application can be run with docker-compose, it has flower dashboard support for Celery and Celery scheduled tasks

# Quick Setup

### Running with docker-compose

1. Create .env file in the root directory

example .env file:

```buildoutcfg
export MODE = 'Prod'
export TOKEN = 'very secret token'
```

2. `docker-composue up --build`

`docker-compose up --build -d` to run in a background

3. If running for the first time

`dokcer exec -it webapp-celery-wroker bash`

`python manage.py recreate_db` (run inside celery container)

This will initialize all db schemas. Postgress container is using docker volume so the data will be stored after exiting or restaring the container

4. check: `localhost:5001/healthcheck`



### Running for development purposes

For development purposes it is possible to run this as a single flask instance and a separate postgress DB
(no celery tasks)

1. Create new virtual environment (see requirements.txt) python 3.6.8

2. Create .env file in the root directory

example .env file:
```buildoutcfg
export MODE = 'Develop'
export TOKEN = 'very secret token'
```

4. Start db instance

`/scripts/start_local_db.sh`

If running for the first time:

`python manage.py recreate_db`

5. `python main.py`

application will run on port 5011

# Running tests

To run pylint and flake-8

`pytest --flake8 --pylint --ignore=webapp/tests --ignore=webapp/common/settings.py`

To run pytest:

Tests can be run directly in the celery worker container:

`docker exec webapp-celery-worker python -m pytest web_app/tests`



