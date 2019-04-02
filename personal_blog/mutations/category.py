# coding=utf8

from graphene import Mutation, String, ObjectType, Field
import graphene
from personal_blog.models.category import Category as CategoryModel
from flask_jwt_extended import current_user, jwt_required
from personal_blog.mutations.core import MutationResponse
from personal_blog.dao import category as dao_category
from personal_blog.types.category import Category


class CreateCategory(Mutation):
    class Meta:
        interfaces = [MutationResponse]

    class Arguments:
        label = String(description="分类名称", required=True)
        desc = String(description="描述")

    category = Field(Category, description="分类详情")

    @jwt_required
    def mutate(self, info, label, desc):
        category = CategoryModel.query.filter(CategoryModel.label == label).first()
        if category:
            return CreateCategory(code=400, message="当前分类名称已被创建", success=False)
        else:
            category = dao_category.category_create(label, desc)
            return CreateCategory(category)


class EditCategory(Mutation):
    class Meta:
        interfaces = [MutationResponse]

    class Arguments:
        id = String(description="分类id", required=True)
        label = String(description="标题")
        desc = String(description="描述")
        is_show = graphene.Boolean(description="是否展示")

    @jwt_required
    def mutate(self, info, id, label, desc, is_show):
        category = Category.get_node(info, id)
        dao_category.category_edit(category.rid, label, desc, is_show)
        return EditCategory()


class DeleteCategory(Mutation):
    class Meta:
        interfaces = [MutationResponse]

    class Arguments:
        id = String(description="分类id")

    @jwt_required
    def mutate(self, info, id):
        category = Category.get_node(info, id)
        dao_category.category_delete(category.rid)


class CategoryMutation(ObjectType):
    category_create = CreateCategory.Field(description="分类创建")
    category_edit = EditCategory.Field(description="分类编辑")
    category_delete = DeleteCategory.Field(description="分类删除")
