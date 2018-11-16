# coding=utf8

from personal_blog.schemas import ma
from personal_blog.schemas.base import BaseMeta
from personal_blog.models.article import Article
from personal_blog.schemas.account_schema import AccountSchema
from personal_blog.schemas.category_schema import CategorySchema


class ArticleSchema(ma):
    class meta(BaseMeta):
        model = Article
        # exclude = ('category_id', 'creator_id')

    id = ma.Str(attribute='id')
    category_id = ma.Str(attribute='category_id')
    creator_id = ma.Str(attribute='creator_id')
    account = ma.Nested(AccountSchema())
    category = ma.Nested(CategorySchema())
