
import graphene
from personal_blog.types.account import Account
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField


class AccountQuery(graphene.ObjectType):
    accounts = SQLAlchemyConnectionField(Account,description="用户列表")

    def resolve_accounts(self,info, args):

        return "aaaaaaa"