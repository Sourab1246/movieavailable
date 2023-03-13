from rest_framework import serializers
from .models import movies

class moviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=movies
        fields=['id','Name','cast','duration','image']