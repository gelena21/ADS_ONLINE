from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователей.
    """

    def create(self, validate_data):
        user = User.objects.create(**validate_data)
        user.set_password(user.password)
        user.save()
        return user



    class Meta:
        model = User
        fields = "__all__"
