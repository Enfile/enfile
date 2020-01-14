from django.shortcuts import render
from rest_framework import viewsets
from .models import TechnologyLevel
from .serializers import TechnologyLevelSerializer


class TechnologyLevelViewSet(viewsets.ModelViewSet):
    queryset = TechnologyLevel.objects.all()
    serializer_class = TechnologyLevelSerializer


