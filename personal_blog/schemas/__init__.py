from graphene import ObjectType, relay
import graphene
from personal_blog.queries import RootQuery
from personal_blog.mutations import RootMutation


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)


