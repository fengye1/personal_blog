# coding=utf8
import sqlalchemy as SA
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, INTEGER, BOOLEAN, TEXT
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from personal_blog.models.base import Base
from personal_blog.models.category import Category


class Article(Base):
    """
    文章表
    """
    __tablename__ = "article"
    id = SA.Column(BIGINT(unsigned=True), autoincrement=True, primary_key=True)
    category_id = SA.Column(BIGINT(unsigned=True), SA.ForeignKey('category.id'))
    creator_id = SA.Column(BIGINT(unsigned=True), SA.ForeignKey('account.id'))
    title = SA.Column(String(128))
    content = SA.Column(TEXT)

