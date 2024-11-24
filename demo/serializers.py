from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'balance']