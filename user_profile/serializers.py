from rest_framework import serializers

from user_profile.models import UserProfile


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = (
            "email",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )
