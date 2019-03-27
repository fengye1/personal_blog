# coding=utf8

from flask import Flask
from personal_blog import views
from personal_blog.config import setting
from personal_blog.models.base import db

from flask_migrate import Migrate
BLUEPRINTS = [
    (views.account_bp, '/account')
]
if setting.DEBUG:
    BLUEPRINTS.append((views.test_bp, '/test'))


def create_app():
    app = Flask(__name__)
    app.config.from_object(setting)
    configure_blueprints(app, BLUEPRINTS)
    configure_db(app)

    return app


def configure_blueprints(app, blueprints):
    # 配置蓝图
    if blueprints:
        for view, url_prefix in blueprints:
            app.register_blueprint(view, url_prefix=url_prefix)


def configure_db(app):
    """配置数据库"""
    db.init_app(app)
    # Migrate
    Migrate(app, db)

