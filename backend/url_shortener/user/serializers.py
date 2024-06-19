# serializers.py

from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'name', 'email', 'username', 'password', 'date_register', 'is_active', 'is_staff',
                  'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password field is write-only
            'is_staff': {'read_only': True},  # Ensure is_staff is read-only
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
