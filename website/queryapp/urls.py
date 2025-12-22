from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('users/', views.list_users, name='list_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('search/', views.search_users, name='search_users'),
]
