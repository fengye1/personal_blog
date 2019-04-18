# coding=utf8

from flask import Flask

from flask_migrate import Migrate
from flask_graphql import GraphQLView
from flask_jwt_extended import JWTManager
from personal_blog.config import setting
from personal_blog.models.base import db
from personal_blog.schemas import schema
from personal_blog import views
from personal_blog.commands.initdata import initdata_cli
from flask_cors import CORS


BLUEPRINTS = [
    (views.frontend_bp, '/'),
]

COMMANDS = [initdata_cli]


def create_app():
    app = Flask(__name__)
    app.config.from_object(setting)
    configure_blueprints(app, BLUEPRINTS)
    jwt = JWTManager(app)
    configure_graphql(app)
    configure_db(app)
    configure_commands(app, COMMANDS)
    CORS(app)
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


def configure_commands(app, commands):
    """注册命令"""
    if commands:
        for command in commands:
            app.cli.add_command(command)
