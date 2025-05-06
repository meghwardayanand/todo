from django.contrib import admin

from todo.models import TodoItem


# Register your models here.
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'status', 'owner')

admin.site.register(TodoItem, TodoItemAdmin)
