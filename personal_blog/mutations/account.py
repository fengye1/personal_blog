# coding=utf8

from graphene import Mutation, String, ObjectType
from personal_blog.models.account import Account as AccountModel
from flask_jwt_extended import create_access_token
from personal_blog.mutations.core import MutationResponse
from flask import jsonify


#
# class CreatePerson(graphene.Mutation):
#     class Arguments:
#         name = graphene.String()
#
#     ok = graphene.Boolean()
#     person = graphene.Field(lambda: Person)
#
#     def mutate(self, info, name):
#         person = Person(name=name)
#         ok = True
#         return CreatePerson(person=person, ok=ok)


class Login(Mutation):
    class Meta:
        interfaces = [MutationResponse]

    class Arguments:
        email = String(description="邮箱", required=True)
        password = String(description="密码", required=True)

    access_token = String(description='登录凭证')

    def mutate(self, info, email, password):
        user = AccountModel.query.filter(AccountModel.email == email).first()
        if not user:
            return Login(code=400, message="没有该用户", success=False)
        if user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return Login(access_token=access_token)
        else:
            return Login(code=400, message="你输入的邮箱或密码错误", success=False)


class AccountMutation(ObjectType):
    login = Login.Field(description="账户登录")
  