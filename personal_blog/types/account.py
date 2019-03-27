# utf-8


from graphene import relay, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from personal_blog.models.account import Account as AccountModel


class Account(SQLAlchemyObjectType):
    class Meta:
        model = AccountModel
        interfaces = (relay.Node,)
        exclude_fields = ("pw_hash",)
    rid = String(description='rid')

    def resolve_rid(self, info):
        return str(self.id)



