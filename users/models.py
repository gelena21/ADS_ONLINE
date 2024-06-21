from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер для пользовательской модели.
    """

    def create_user(self, email, first_name, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с указанным email и паролем.
        """
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        """
        Создает и возвращает суперпользователя с указанным email и паролем.
        """
        user = self.create_user(email, first_name=first_name, password=password, **extra_fields)
        user.is_active = True
        user.is_admin = True
        user.role = 'ADMIN'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    Кастомная модель пользователя.
    """
    username = None
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    role = models.CharField(max_length=150, verbose_name='Роль', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """
        Проверяет, имеет ли пользователь данное разрешение.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Проверяет, имеет ли пользователь разрешения на модуль.
        """
        return self.is_admin

    @property
    def is_admin(self):
        """
        Проверяет, является ли пользователь администратором.
        """
        return self.role == 'ADMIN'

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
