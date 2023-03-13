from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
# from django.contrib.auth.decorators import login_required
from .models import movies

from django.db.models import Count
from .serializers import moviesSerializer

class movies(viewsets.ModelViewSet):
     queryset = movies.objects.all()
     serializer_class = moviesSerializer
   