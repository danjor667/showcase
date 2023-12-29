from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('projects/', include('projects.urls')),
    path('profiles/', include('users.urls')),
]