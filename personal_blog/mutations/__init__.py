# coding=utf8

from graphene import ObjectType
from personal_blog.mutations.account import AccountMutation
from personal_blog.mutations.category import CategoryMutation
from personal_blog.mutations.article import ArticleMutation


class RootMutation(AccountMutation, CategoryMutation, ArticleMutation, ObjectType):
    pass
