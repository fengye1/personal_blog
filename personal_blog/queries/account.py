import graphene
from graphene import Field
from personal_blog.types.account import Account
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


class AccountQuery(graphene.ObjectType):
    account = Field(Account)
    accounts = SQLAlchemyConnectionField(Account, description="用户列表")

    def resolve_accounts(self, info, args):
        return Account.get_query(info)
