# blog/urls.py
from django.urls import path
from django.contrib import admin
from . import views
from .admin import admin_site
from django.conf.urls.static import static
from django.conf import settings


app_name = 'chatgpt'
urlpatterns = [

    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('admin/', admin_site.urls),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
