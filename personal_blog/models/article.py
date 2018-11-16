# coding=utf8
import sqlalchemy as SA
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, INTEGER, BOOLEAN, TEXT
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from personal_blog.models.base import Base, id_generate


class Article(Base):
    """
    文章表
    """
    __tablename__ = "article"
    id = SA.Column(BIGINT(unsigned=True), default=id_generate(), primary_key=True)
    category_id = SA.Column(BIGINT(unsigned=True), SA.ForeignKey('category.id'))
    creator_id = SA.Column(BIGINT(unsigned=True), SA.ForeignKey('account.id'))
    title = SA.Column(String(128))
    content = SA.Column(TEXT)

