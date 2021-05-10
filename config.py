import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "sshh!"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    # os.environ.get("DATABASE_URL") or
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "tests/test.db")
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #in memory database
