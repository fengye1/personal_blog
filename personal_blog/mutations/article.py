# coding=utf8

from graphene import Mutation, String, ObjectType, Field
import graphene
from personal_blog.models.article import Article as ArticleModel
from flask_jwt_extended import current_user, jwt_required
from personal_blog.mutations.core import MutationResponse
from personal_blog.dao import article as dao_article
from personal_blog.types.article import Article


class AddOrUpdateArticle(Mutation):
    class Meta:
        interfaces = [MutationResponse]

    class Arguments:
        id = String(description="文章id", required=False)
        title = String(description="文章名称", required=True)
        category_id = String(description="所属分类id", required=True)
        content = String(description="内容")

    # article = Field(Article, description="添加文章")

    # @jwt_required
    def mutate(self, info, title, content,category_id, id=None):
        print("===========>", title, content, category_id, id)
        article = dao_article.update_article(title, content, category_id, id)
        if article:
            return AddOrUpdateArticle()
        else:
            return AddOrUpdateArticle(code=400, message="标题不能重复", success=False)


class DeleteArticle(Mutation):
    class Meta:
        interfaces = [MutationResponse]

    class Arguments:
        id = String(description="文章id")

    @jwt_required
    def mutate(self, info, id):
        dao_article.delete_article()
        return DeleteArticle()


class ArticleMutation(ObjectType):
    article_edit = AddOrUpdateArticle.Field(description="文章创建或更新")
    article_delete = DeleteArticle.Field(description="文章删除")
