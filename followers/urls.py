from django.urls import path

from followers.views import AddFollowerView, ListFollowerView, ListFoollowingView, RemoveFollowerView


urlpatterns = [
    path('followers/', ListFollowerView.as_view(), name='list-followers'),
    path('following/', ListFoollowingView.as_view(), name='list-following'),
    path('add/<int:pk>/', AddFollowerView.as_view(), name='add-follower'),
    path('delete/<int:pk>/', RemoveFollowerView.as_view(), name='delete-follower')
]
