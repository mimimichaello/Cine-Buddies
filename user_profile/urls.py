from django.urls import path
from user_profile.views import UserListAPIView, ProfileAPIView


urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('profile/<int:pk>', ProfileAPIView.as_view(), name='user-profile'),
]

