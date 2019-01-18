# coding=utf8

from graphene import Mutation, String
from personal_blog.models.account import Account as AccountModel

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
    class Arguments:
        email = String(description="邮箱")
        passwd = String(description="密码")

    access_token = String(description='登录凭证')
    def mutate(self, info, email, passwd):
        user = AccountModel.query.filter(AccountModel.email==email).first()
        if user.check_password(passwd):
            pass



