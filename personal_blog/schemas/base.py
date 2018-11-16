# coding=utf8

from flask_marshmallow import Marshmallow
ma = Marshmallow()


class BaseMeta(object):
    dateformat = '%Y-%m-%d %H:%M:%S'

