from django.db import models
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Movie
from .serializers import FavoriteSerializer

class FavoriteList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = FavoriteSerializer

