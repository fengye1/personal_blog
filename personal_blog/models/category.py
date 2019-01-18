# coding=utf8
import sqlalchemy as SA
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, INTEGER, BOOLEAN, TEXT
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from personal_blog.models.base import Base
from personal_blog.models.article import Article

class Category(Base):
    """
    分类表
    """
    __tablename__ = 'category'


    label = SA.Column(String(32))
    position = SA.Column(INTEGER, default=1, autoincrement=True)
    is_show = SA.Column(BOOLEAN, default=True)
