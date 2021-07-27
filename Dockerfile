# Our docker-compose file uses Dockerfile-dev instead of Dockerfile
FROM python:3.6.8

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x /app/scripts/docker_script.sh
ENV FLASK_ENV=docker
#EXPOSE 5000