# coding=utf8
import sqlalchemy as SA
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, INTEGER, BOOLEAN, TEXT
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from personal_blog.models.base import Base, id_generate
from personal_blog.models.article import Article

class Category(Base):
    """
    分类表
    """
    __tablename__ = 'category'

    id = SA.Column(BIGINT(unsigned=True), default=id_generate(), primary_key=True)
    label = SA.Column(String(32))
    position = SA.Column(INTEGER, default=1, autoincrement=True)
    is_show = SA.Column(BOOLEAN, default=True)
    articles = relationship("Article", backref='category', cascade="all, delete")
