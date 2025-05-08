from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets

from todo.models import TodoItem
from todo.serializers import TodoItemSerializer

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated|IsAdminUser]
    serializer_class = TodoItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        logged_user = self.request.user
        if logged_user.is_superuser or logged_user.is_staff:
            return queryset

        return queryset.filter(owner_id=logged_user.id)
