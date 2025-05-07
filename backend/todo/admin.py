from django.contrib import admin

from todo.models import TodoItem


# Register your models here.
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'status', 'owner')
    search_fields = ['title']
    list_filter = ('status', 'owner')
    list_per_page = 10

admin.site.register(TodoItem, TodoItemAdmin)
