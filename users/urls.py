from django.urls import path
from . import views


# /api/profiles/
urlpatterns = [
    path('', views.list_create, name="profiles"),
    path('<int:pk>/', views.profile_update, name="profile-details"),
    path('<str:pk>/update/', views.profile_update, name='update-profile'),
    path('<str:pk>/delete/', views.profile_update, name='create-profile')
]