from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from films.serializers import FilmSerializer
from films.models import Film

from films.pagination import FilmListPagination



class FilmListView(generics.ListAPIView):
    """Получение списка фильмов
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = FilmListPagination


class FilmAPIView(APIView):
    """Получение информации о фильме
    """
    def get(self, request, pk):
        film = Film.objects.filter(id=pk).first()
        if film:
            serializer = FilmSerializer(film)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Film not found', status=status.HTTP_404_NOT_FOUND)




class FilmFilterView(generics.ListAPIView):
    """Фильтрация фильмов
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = FilmListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'release_date', 'rating', 'genre',]
