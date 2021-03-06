# coding=utf8

from personal_blog.config.base import *

DEBUG=True


MAIN_HOST="127.0.0.1"
MAIN_DB = {
    'host': MAIN_HOST,
    'db_name': 'personal_blog',
    'user': 'personal_blog',
    'password': '123456',
}

# CREATE SCHEMA `cooperation` DEFAULT CHARACTER SET utf8 ;
MAIN_DB_URI = 'mysql://%s:%s@%s/%s?charset=utf8' % (MAIN_DB['user'], MAIN_DB['password'], MAIN_DB['host'], MAIN_DB['db_name'])

# SQLAlchemy Config
SQLALCHEMY_DATABASE_URI = MAIN_DB_URI
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 120
SQLALCHEMY_POOL_RECYCLE = 360

JWT_SECRET_KEY = 'personal_blog'
