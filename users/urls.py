from django.urls import path
from . import views

# /api/profile/
# /api/user/
urlpatterns = [
    path('', views.list, name="user"),
    path('create/', views.generic_create, name="create"),
    path('<int:pk>/', views.list, name="user-details"),
    path('<str:pk>/update/', views.generic_update_delete),
    path('<str:pk>/delete/', views.generic_update_delete),
    #profiles  todo correct the profile path
    #path('', views.list_profile)
    #path('<str:pk>/, views.list_profile)
    #path('<str:pk>/update/', views.update)
]