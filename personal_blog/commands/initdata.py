from flask.cli import AppGroup

from personal_blog.dao.account import create_user
from personal_blog.models.base import db
import click

initdata_cli = AppGroup("initdata")


@initdata_cli.command("create_admin")
def create_admin():
    email = "2@qq.com"
    name = 'admin'
    password = "111111"
    create_user(name, email, password, True)
    click.echo("创建管理员成功")
