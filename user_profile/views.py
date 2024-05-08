from rest_framework import generics
from rest_framework import permissions
from user_profile.models import UserProfile
from user_profile.serializers import ProfileUserSerializer, PublicUserSerializer
from django_filters.rest_framework import DjangoFilterBackend

from user_profile.pagination import UserListPagination



class UserListAPIView(generics.ListAPIView):
    """
    Вывод списка пользователей
    """
    queryset = UserProfile.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email', ]
    pagination_class = UserListPagination


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    Профайл пользователя
    """
    serializer_class = ProfileUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)
