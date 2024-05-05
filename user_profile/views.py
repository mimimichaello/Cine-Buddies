from rest_framework import generics
from user_profile.models import UserProfile
from user_profile.serializers import ProfileUserSerializer, PublicUserSerializer
from rest_framework import permissions



class UserListAPIView(generics.ListAPIView):
    """
    Вывод списка пользователей
    """
    queryset = UserProfile.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = (permissions.AllowAny,)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    Профайл пользователя
    """
    serializer_class = ProfileUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)
