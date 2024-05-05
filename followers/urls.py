from django.urls import path

from followers.views import AddFollowerView, ListFollowerView


urlpatterns = [
    path('', ListFollowerView.as_view(), name='list-subscribers'),
    path('add/<int:pk>/', AddFollowerView.as_view(), name='add-follower'),
]
