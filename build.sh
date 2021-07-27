#!/bin/bash
docker-compose up -d --build || { echo 'docker-compose up failed' ; exit 1;}
docker exec webapp-celery-worker python -m pytest web_app/tests || { echo 'PYTESTS FAILED' ; exit 1;}
docker system prune -f
