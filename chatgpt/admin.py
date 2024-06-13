from django.contrib import admin
from django.urls import path
from .models import ChatHistory

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

# Register your models here.

class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'timestamp')
    search_fields = ('question', 'answer')
    list_filter = ('timestamp',)

admin.site.register(ChatHistory, ChatHistoryAdmin)

class MyAdminSite(AdminSite):
    site_header = _("My Admin")
    site_title = _("My Admin Portal")
    index_title = _("Welcome to My Admin")

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('custom_admin/', self.admin_view(self.custom_admin_view)),
        ]
        return my_urls + urls

    def custom_admin_view(self, request):
        from django.shortcuts import render
        return render(request, 'admin/custom_admin.html')

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/custom_admin.css'
        context['custom_js'] = 'js/custom_admin.js'
        return context

admin_site = MyAdminSite(name='myadmin')