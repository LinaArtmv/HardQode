from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]
