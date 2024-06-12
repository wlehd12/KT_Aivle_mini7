# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchQA/', views.searchDB, name='aivleQA'),
]
