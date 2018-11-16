# coding=utf8

from personal_blog.models.account import Account
from personal_blog.models.base import db


def dao_register_account(emial, password, name):
    """
    注册账号
    :param emial:
    :param password:
    :param name:
    :return:
    """

    account = Account.query.filter(Account.email == emial).first()
    if not account:
        account = Account(emial=emial, name=name)
        account.set_password_hash(password)
        db.session.add(account)
        db.session.commit()
        return account
    return None


def dao_login(email, password):
    """
    账号登录
    :param email:
    :param password:
    :return:
    """
    user = Account.query.filter(Account.email == email).first()
    if not user or not user.check_password(password):
        return None
    return user
