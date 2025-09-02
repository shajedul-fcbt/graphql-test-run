
from ctypes import cast
from typing import Optional
from django.db.models import query
import strawberry_django
import strawberry
from django.contrib.auth import get_user_model
from logbook.models import MessageModel
from typing import List 



UserModel = get_user_model()

@strawberry_django.type(UserModel)
class GUser:
    id: strawberry.ID
    username: strawberry.auto
    messages: List["Message"] = strawberry_django.field()


@strawberry_django.type(MessageModel)
class Message:
    id: strawberry.ID
    content: strawberry.auto
    created_at: strawberry.auto
    author: GUser = strawberry_django.field()


@strawberry.type
class Query:
    user: List[GUser] = strawberry_django.field()


    @strawberry_django.field
    def messages(self, limit: int = 50, offset: int=  0) -> List[Message]:
            qs = MessageModel.objects.order_by("-created_at")[offset: offset + limit]
            return qs

    @strawberry_django.field
    def user(self, id: strawberry.ID) -> Optional[GUser]:
        return UserModel.objects.filter(id=id).first()


    @strawberry_django.field
    def message(self, id: strawberry.ID) -> Optional[Message]:
        return MessageModel.objects.filter(id=id).firtst()


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_user(self, username: str, password: str) -> GUser:   
        user = UserModel.objects.create_user(username = username, password = password)

        return User.from_django(user)

    @strawberry.mutation
    def post_message(self, author_id: strawberry.ID, content: str) -> Message:
        content = content.strip()
        if not content:
            raise ValueError("Content cannot be empty")

        print("I am Here")

        author = UserModel.objects.get(id= author_id).first()
        if not author:
            raise ValueError("author could not be found")
        

        msg = MessageModel.objects.create(author= author, content = content)
        return msg


schema = strawberry.Schema(query= Query, mutation=Mutation)










