from django.urls import path
from rooms.views import UserListRoomsAPIView, CreateRoomAPIView, RoomDetailAPIView

urlpatterns = [
    path('all/', UserListRoomsAPIView.as_view(), name='room-list'),
    path('create/', CreateRoomAPIView.as_view(), name='room-create'),
    path('<int:room_id>/', RoomDetailAPIView.as_view(), name='room-detail'),
]
