# coding=utf8

from personal_blog.schemas import ma
from personal_blog.schemas.base import BaseMeta
from personal_blog.models.category import Category
from personal_blog.schemas.article_schema import ArticleSchema


class CategorySchema(ma.ModelSchema):
    class meta(BaseMeta):
        model = Category

    id = ma.Str(attribute='id')
    articles = ma.Nested(ArticleSchema(), many=True)


