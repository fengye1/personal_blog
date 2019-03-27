#coding:utf-8
from graphene import ObjectType

from personal_blog.queries.account import AccountQuery


class RootQuery(AccountQuery, ObjectType):
    pass
