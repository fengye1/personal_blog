# coding=utf8
import sqlalchemy as SA
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, BOOLEAN
from sqlalchemy.types import String

from personal_blog.models.base import Base


class Category(Base):
    """
    分类表
    """
    __tablename__ = 'category'
    id = SA.Column(BIGINT(unsigned=True), autoincrement=True, primary_key=True)
    label = SA.Column(String(32))
    position = SA.Column(INTEGER, default=1, autoincrement=True)
    is_show = SA.Column(BOOLEAN, default=True)
