# coding=utf8

import sqlalchemy as SA
from sqlalchemy.types import String, BOOLEAN
from personal_blog.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash


class Account(Base):
    """账户表"""
    __tablename__ = 'account'
    name = SA.Column(String(32))
    email = SA.Column(String(32))
    pw_hash = SA.Column(String(128))
    avatar_id = SA.Column(String(128))
    is_admin = SA.Column(BOOLEAN, default=True)

    def set_password_hash(self, pw, **kwargs):
        self.pw_hash = generate_password_hash(pw, salt_length=16)

    def check_password(self, pw):
        return check_password_hash(self.pw_hash, pw)
