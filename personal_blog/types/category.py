
from graphene import String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from personal_blog.models.category import Category as CategoryModel


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node,)

    rid = String(description='rid')

    def resolve_rid(self, info):
        return str(self.id)
