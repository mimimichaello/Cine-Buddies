from django.urls import path

from films.views import ExternalMovieData


urlpatterns = [
    path('movie/<int:pk>/', ExternalMovieData.as_view(), name='movie'),
    #path('movies/', ExternalMovieDataList.as_view(), name='movies'),
]
