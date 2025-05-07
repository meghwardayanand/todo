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
<<<<<<< HEAD
        request = self.context.get('request')
        validated_data['owner'] = request and request.user
=======
        validated_data['owner'] = self.context['request'].user
>>>>>>> b5be0326a47038e4b2a686c8cb863ea0219b4cd6
        todo_item = TodoItem.objects.create(**validated_data)
        return todo_item
