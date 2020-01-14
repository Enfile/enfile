from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer, UserFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter

