# from graphene import ObjectType, relay
import graphene


# class Query(graphene.ObjectType):
#     node = relay.Node.Field()


# schema = graphene.Schema(query=Query)

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument


schema = graphene.Schema(query=Query)

