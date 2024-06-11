from django.urls import path
from django.contrib import admin
from . import views

app_name = 'selfchatgpt'
urlpatterns = [

    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('history/', views.chat_history, name='chat_history'),
    path('clear_history/', views.clear_history, name='clear_history'),
]
