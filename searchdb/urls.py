# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]
