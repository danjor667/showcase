from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('<str:pk>/', views.profile_details, name="profile-details"),
]