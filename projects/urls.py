from django.urls import path
from . import views


# /api/projects/
urlpatterns = [
    path('', views.generic_list_create),
    path('<str:pk>/', views.generic_get_update_delete, name="project"),
    path('<str:pk>/update/', views.generic_get_update_delete, name="update"),
    path('<str:pk>/delete/', views.generic_get_update_delete, name="delete"),
]