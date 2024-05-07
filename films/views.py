from datetime import datetime
import os
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



class ExternalMovieData(APIView):
    def get(self, request, pk):
        api_key = os.environ.get('API_KEY')
        movie_api_url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{pk}'

        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json',
        }

        response = requests.get(movie_api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            release_year = data.get('year')
            release_date = datetime(int(release_year), 1, 1).strftime('%Y-%m-%d')

            movie_serializer = MovieSerializer(data={
                'title': data.get('nameRu'),
                'description': data.get('description'),
                'poster_img_url': data.get('posterUrl'),
                'release_date': release_date,
                'rating': data.get('ratingKinopoisk'),
                'genre': ', '.join([genre['genre'] for genre in data.get('genres', [])]),
                'external_id': data.get('kinopoiskId'),
            })

            if movie_serializer.is_valid():
                movie_serializer.save()
                return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExternalMovieDataList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
