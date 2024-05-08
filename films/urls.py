from django.urls import path
from films.views import FilmAPIView, FilmListView, FilmFilterView



urlpatterns = [
    path('<int:pk>/', FilmAPIView.as_view(), name='film'),
    path('all/', FilmListView.as_view(), name='all-films'),
    path('filters/', FilmFilterView.as_view(), name='filters'),
]
