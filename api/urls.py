from django.urls import path, include
from . import views
from users.views import generic_create


urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('auth/', views.obtain_auth_token),
    path('auth/register/', generic_create),
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
]