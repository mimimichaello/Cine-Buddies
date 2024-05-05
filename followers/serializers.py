from rest_framework import serializers
from followers.models import Follower
from user_profile.models import UserProfile


class UserByFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'profile_picture',)



class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(many=False, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)
