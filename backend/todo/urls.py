from django.urls import path

from todo.views import TodoItemViewSet


app_name='todo'
urlpatterns = [
    path("todos/", TodoItemViewSet.as_view({
        "get": "list",
        'post': "create",
    }), name="todos-create"),

    path("todos/<int:pk>/", TodoItemViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }), name="todos-detail"),
]
