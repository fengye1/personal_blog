import graphene
from graphene import Field
from personal_blog.types.category import Category
from graphene_sqlalchemy import SQLAlchemyConnectionField


class CategoryQuery(graphene.ObjectType):
    category = Field(Category, description="分类")
    categories = SQLAlchemyConnectionField(Category, description="分类列表")

    def resolve_category(self, info):
        return Category.get_query(info).first()

    def resolve_categories(self, info, args):
        return Category.get_query(info)
