from rest_framework import serializers

from todo.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TodoItem
        fields = '__all__'
        extra_kwargs = {
            "owner": {
                "required": False
            }
        }


    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request and request.user
        todo_item = TodoItem.objects.create(**validated_data)
        return todo_item
