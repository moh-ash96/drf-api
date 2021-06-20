from favorites.models import Movie
from rest_framework import serializers

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'rate', 'release', 'genre', 'admin',)