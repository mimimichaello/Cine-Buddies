from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from user_profile.models import UserProfile
from followers.serializers import ListFollowerSerializer
from followers.models import Follower


class ListFollowerView(generics.ListAPIView):
    """Список подписчиков"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscribed_to=self.request.user)

class AddFollowerView(views.APIView):
    """Добавление в подписки"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserProfile.objects.filter(id=pk).first()
        if user:
            Follower.objects.create(subscriber=request.user, subscribed_to=user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
