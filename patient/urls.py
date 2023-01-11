from django.urls import path
from patient import views

# TEMPLATE URLs
# app_name = 'patient'

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='login'),
    path('register/', views.register_user, name='register'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('delete_user/', views.delete_user, name='delete_user'),
]
