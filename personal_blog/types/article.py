
from graphene import String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from personal_blog.models.article import Article as ArticleModel


class Article(SQLAlchemyObjectType):
    class Meta:
        model = ArticleModel
        interfaces = (relay.Node,)

    rid = String(description='rid')

    def resolve_rid(self, info):
        return str(self.id)
