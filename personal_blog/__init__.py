# coding=utf8

from flask import Flask

from personal_blog.config import setting
from personal_blog.models.base import db
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from  personal_blog.schemas import schema


def create_app():
    app = Flask(__name__)
    app.config.from_object(setting)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',schema=schema, grqphiql=True))
    configure_db(app)
    return app

def configure_db(app):
    """配置数据库"""
    db.init_app(app)
    # Migrate
    Migrate(app, db)

