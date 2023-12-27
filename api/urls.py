from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints, name="endpoints"),
    path('projects/', views.projects, name="create_update"),
    path('projects/create/', views.projects, name="projects"),
    path('projects/<str:pk>/', views.update_delete, name="projects"),
    path('projects/<str:pk>/update/', views.update_delete, name="update"),
    path('projects/<str:pk>/delete/', views.update_delete, name="update"),
]