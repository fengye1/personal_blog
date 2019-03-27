# coding=utf8
import sqlalchemy as SA
from sqlalchemy.dialects.mysql import  TEXT
from sqlalchemy.types import String
from sqlalchemy.dialects.mysql import BIGINT
from personal_blog.models.base import Base


class Article(Base):
    """
    文章表
    """
    __tablename__ = "article"
    id = SA.Column(BIGINT(unsigned=True), autoincrement=True, primary_key=True)
    category_id = SA.Column(BIGINT(unsigned=True))
    creator_id = SA.Column(BIGINT(unsigned=True))
    title = SA.Column(String(128))
    content = SA.Column(TEXT)

