# coding=utf8

from graphene import ObjectType
from personal_blog.mutations.account import AccountMutation
from personal_blog.mutations.category import CategoryMutation


class RootMutation(AccountMutation, CategoryMutation, ObjectType):
    pass

