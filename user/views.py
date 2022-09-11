from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.api.serializers import UserSerializer

class RegisterView(CreateAPIView) :
    serializer_class = UserSerializer

