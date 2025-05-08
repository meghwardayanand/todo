from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


class SignUpUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        confirm_password = attrs.pop('confirm_password', '')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Duplicate user!')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages
            )

        # Password validations can be done here.
        if password != confirm_password:
            raise serializers.ValidationError('Password mismatch!')

        # After all password validations, make hash.
        attrs['password'] = make_password(attrs['password'])

        return attrs

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UserSignInSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs.get('username','')
        password = attrs.get('password','')

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'user': user,
            'username': user.username,
        }
