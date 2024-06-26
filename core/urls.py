from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Cine Buddies API",
      default_version='v1',
      description="Cine Buddies API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/users/', include('user_profile.urls')),
   path('api/v1/subscriptions/', include('followers.urls')),
   path('api/v1/film/', include('films.urls')),
   path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
