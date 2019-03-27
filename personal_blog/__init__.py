# coding=utf8

from flask import Flask

from personal_blog.config import setting
from personal_blog.models.base import db
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from  personal_blog.schemas import schema
from personal_blog import views
BLUEPRINTS = [
    (views.frontend_bp, '/'),
]

def create_app():
    app = Flask(__name__)
    app.config.from_object(setting)
    configure_blueprints(app, BLUEPRINTS)

    configure_graphql(app)
    configure_db(app)
    return app

def configure_db(app):
    """配置数据库"""
    db.init_app(app)
    # Migrate
    Migrate(app, db)

def configure_blueprints(app, blueprints):
    # 注册蓝图
    if blueprints:
        for view, url_prefix in blueprints:
            app.register_blueprint(view, url_prefix=url_prefix)


def configure_graphql(app):
    """配置graphql"""
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql', schema=schema, graphiql=app.debug))



