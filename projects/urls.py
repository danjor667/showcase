from django.urls import path
from . import views


# /api/projects/
urlpatterns = [
    path('', views.generic_list),
    path('create/', views.generic_create),
    path('<str:pk>/', views.generic_list, name="project"),
    path('<str:pk>/update/', views.generic_update_delete, name="update"),
    path('<str:pk>/delete/', views.generic_update_delete, name="delete"),
]