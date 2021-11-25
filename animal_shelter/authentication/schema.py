# from datetime import date

# import graphene
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import Group
# from graphene_django import DjangoObjectType
# from graphql_auth import mutations
# from graphql_auth.schema import MeQuery
# from graphql_jwt.decorators import login_required

# from .decorators import is_admin

# # from .groups_schema import GroupQuery
# from .models import User


# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = "__all__"


# class Query(MeQuery, graphene.ObjectType):  # GroupQuery

#     users = graphene.List(UserType)
#     user = graphene.Field(UserType, id=graphene.Int())

#     @login_required
#     @is_admin
#     def resolve_users(root, info):
#         return User.objects.all()

#     @login_required
#     @is_admin
#     def resolve_user(root, info, id):
#         return User.objects.get(id=id)

# class AuthMutation(graphene.ObjectType):
#     token_auth = mutations.ObtainJSONWebToken.Field()
#     verify_token = mutations.VerifyToken.Field()
#     refresh_token = mutations.RefreshToken.Field()

# class CreateUser(graphene.Mutation):
#     class Arguments:
#         username = graphene.String(required=True)
#         email = graphene.String(required=True)
#         first_name = graphene.String(required=True)
#         surname = graphene.String(required=True)
#         password = graphene.String(required=True)
#         phone = graphene.String(required=True)
#         city = graphene.String(required=True)
#         zip_code = graphene.String(required=True)
#         address_line1 = graphene.String(required=True)
#         address_line2 = graphene.String(required=False)

#     user = graphene.Field(UserType)

#     @classmethod
#     def mutate(cls, root, username, email, password, first_name, surname)

# class UserToWorker(graphene.Mutation):
#     pass
