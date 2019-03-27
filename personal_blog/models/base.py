# coding=utf8
import sqlalchemy as SA
import datetime
import os
import threading
import time

from personal_blog.config import setting
from flask_sqlalchemy import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIGINT


class tBase(object):
    created_date = SA.Column(SA.DateTime, default=datetime.datetime.now)
    modified_date = SA.Column(SA.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        m = self.__class__.__module__
        c = self.__class__.__name__
        return "<%s.%s id=%s>" % (m, c, self.id)




Base = declarative_base(cls=tBase)

db = SQLAlchemy(model_class=Base, session_options={"enable_baked_queries": True})
metadata = db.metadata


