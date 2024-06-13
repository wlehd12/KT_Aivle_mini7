"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

def index(request):
    return render(request,'index.html')

urlpatterns = [
    path('',index),
    path('chatgpt/',include('chatgpt.urls')),
    path('admin/', admin.site.urls),
    path('selfchatgpt/',include('selfchatgpt.urls')),
    path('accounts/', include('accounts.urls')),
    path('searchdb/', include('searchdb.urls')),
    path('about/', views.about, name ="about"),
    path('index/', views.home_index, name="home_index"),
    path('searchdb/upload_csv', include('searchdb.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)