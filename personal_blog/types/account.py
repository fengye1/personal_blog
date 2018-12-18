#utf-8

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from personal_blog.models.account import Account as AccountModel

class Account(SQLAlchemyObjectType):
    class Meta:
        model = AccountModel
        interfaces = [relay.Node]