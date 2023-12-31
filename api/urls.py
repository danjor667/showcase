from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('auth/', views.obtain_auth_token),
    path('projects/', include('projects.urls')),
    path('profiles/', include('users.urls')),
]