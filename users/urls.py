from django.urls import path
from . import views

# /api/profile/
# /api/user/
urlpatterns = [
    path('', views.list, name="user"),
    path('<int:pk>/', views.list, name="user-details"),
    path('<str:pk>/update/', views.generic_update_delete),
    path('<str:pk>/delete/', views.generic_update_delete),
]