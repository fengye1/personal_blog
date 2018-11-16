# coding=utf8
from personal_blog.schemas import ma
from personal_blog.schemas.base import BaseMeta
from personal_blog.models.account import Account
from personal_blog.schemas.article_schema import ArticleSchema


class AccountSchema(ma.ModelSchema):
    class Meta(BaseMeta):
        model = Account
        exclude = ('pw_hash', 'avatar_id')
    id = ma.Str(attribute='id')
    articles = ma.Nested(ArticleSchema(), many=True)


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
