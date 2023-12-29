from django.urls import path
from . import views


# /api/projects/
urlpatterns = [
    path('', views.list_create),
    path('<str:pk>/', views.update_delete, name="project"),
    path('<str:pk>/update/', views.update_delete, name="update"),
    path('<str:pk>/delete/', views.update_delete, name="delete"),
]