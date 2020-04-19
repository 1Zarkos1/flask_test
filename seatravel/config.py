from os import environ
from dotenv import load_dotenv

load_dotenv('seatravel/.env')

class Config:
    """Base config"""
    SECRET_KEY = environ.get('SECRET_KEY')
    DEBUG = True
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    LANGUAGES = ['en', 'es']

    """DB config"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///maindb.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """SMTP config"""
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = int(environ.get('MAIL_PORT'))
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    ADMINS = ['zarkos@mail.ru']

    """Custom config"""
    POSTS_PER_PAGE = 5
    MS_TRANSLATOR_KEY = environ.get('MS_TRANSLATOR_KEY')