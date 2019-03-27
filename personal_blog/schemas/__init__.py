

import graphene
from personal_blog.queries import RootQuery

schema = graphene.Schema(query=RootQuery)