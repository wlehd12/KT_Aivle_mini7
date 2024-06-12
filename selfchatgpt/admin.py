from django.contrib import admin
from .models import ChatHistory

# Register your models here.
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'timestamp')
    search_fields = ('question', 'answer')
    list_filter = ('timestamp',)

admin.site.register(ChatHistory, ChatHistoryAdmin)