
import graphene
from graphene import Field
from personal_blog.types.account import Account
from graphene_sqlalchemy import SQLAlchemyConnectionField
from flask_jwt_extended import jwt_required, get_jwt_identity


class AccountQuery(graphene.ObjectType):
    current_user = Field(Account, description="当前用户")
    users = SQLAlchemyConnectionField(Account,description="用户列表")

    def resolve_current_user(self, info):
        return Account.get_query(info).first()

    @jwt_required
    def resolve_users(self,info, *args):
        return Account.get_query(info)
