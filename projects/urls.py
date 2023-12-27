from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/<str:pk>/", views.home_detail, name="home-detail"),
]