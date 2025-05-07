from django.contrib import admin

from todo.models import TodoItem


# Register your models here.
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'status', 'owner')
<<<<<<< HEAD
    search_fields = ['title']
    list_filter = ('status', 'owner')
    list_per_page = 10
=======
>>>>>>> b5be0326a47038e4b2a686c8cb863ea0219b4cd6

admin.site.register(TodoItem, TodoItemAdmin)
