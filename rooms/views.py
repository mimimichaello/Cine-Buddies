from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework import permissions

from rest_framework.response import Response
from rest_framework import status

from rooms.models import Room
from rooms.serializers import RoomSerializer

from rooms.permissions import IsRoomOwner


class UserListRoomsAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(owner=user)



class CreateRoomAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(status=status.HTTP_201_CREATED)


class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated, IsRoomOwner)


    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            raise Http404
        return obj
