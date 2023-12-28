from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints, name="endpoints"),
    path('projects/', views.projects, name="create"),
    path('projects/<str:pk>/', views.update_delete, name="project"),
    path('projects/<str:pk>/update/', views.update_delete, name="update"),
    path('projects/<str:pk>/delete/', views.update_delete, name="delete"),

    path('profiles/', views.profiles, name='create'),
    path('profiles/<str:pk>/', views.profile_update),
    path('profiles/<str:pk>/delete/', views.profile_update),
    path('profiles/<str:pk>/update/', views.profile_update)
]