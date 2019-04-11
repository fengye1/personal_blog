# coding:utf-8
from graphene import ObjectType

from personal_blog.queries.account import AccountQuery
from personal_blog.queries.category import CategoryQuery
from personal_blog.queries.article import ArticleQuery


class RootQuery(AccountQuery, ArticleQuery, CategoryQuery, ObjectType):
    pass
