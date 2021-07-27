import sys
from os import path, makedirs

from dataclasses import dataclass
from environs import Env

# Env variable config

ENV_FILE = './.env'

if path.exists(ENV_FILE):
    envir = Env()
    envir.read_env()
else:
    print("Error: .env file not found")
    sys.exit(1)

TOKEN = envir('TOKEN')

LOGGING_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
DATA_FMT = '%y.%b.%d %H:%M:%S'

LOGGING_FILE = "logs/logs.log"

if not path.exists("logs"):
    makedirs("logs")


@dataclass
class Config:
    testing = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


@dataclass
class Develop(Config):
    """Develop loader"""
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://testusr:password@localhost:5433/testdb"
    )


@dataclass
class Prod(Config):
    """ Testing loader """
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://testusr:password@postgres:5432/testdb"
    )
