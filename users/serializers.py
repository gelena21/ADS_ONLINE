from rest_framework import serializers
from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователей.
    """

    class Meta:
        model = User
        fields = '__all__'
