from datetime import datetime

from django.shortcuts import render

from rest_framework import viewsets

from users.serializers import UserSerializer
from users.models import User

from .utils import get_logged_users

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    model = User
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return get_logged_users()

