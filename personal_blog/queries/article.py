import graphene
from graphene import Field
from personal_blog.types.article import Article
from graphene_sqlalchemy import SQLAlchemyConnectionField


class ArticleQuery(graphene.ObjectType):
    article = Field(Article, description="文章")
    articles = SQLAlchemyConnectionField(Article, description="文章列表")

    def resolve_article(self, info):
        return Article.get_query(info).first()

    def resolve_articles(self, info, *args):
        return Article.get_query(info)
