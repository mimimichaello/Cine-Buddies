from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user_profile.models import UserProfile
from django.utils.translation import gettext_lazy as _

class UserProfileAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "profile_picture", "user_permissions")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
    )

admin.site.register(UserProfile, UserProfileAdmin)
