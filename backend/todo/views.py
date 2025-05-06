from rest_framework import permissions
from rest_framework import viewsets

from todo.models import TodoItem
from todo.serializers import TodoItemSerializer

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

