from rest_framework import serializers
from films.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'description', 'poster_img_url', 'release_date', 'rating', 'genre', 'external_id',
            )
