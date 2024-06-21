from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешение для проверки, является ли пользователь владельцем объекта или администратором.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверка прав доступа на уровне объекта.

        Аргументы:
        request (HttpRequest): Текущий HTTP запрос.
        view (APIView): Текущее представление.
        obj (Model): Объект модели, для которого проверяются права.

        Возвращает:
        bool: True, если пользователь имеет доступ, иначе False.
        """
        if request.user == obj.user:
            return True
        return False


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """
    Разрешение для предоставления полного доступа только администраторам, остальные пользователи имеют доступ только на чтение.
    """

    def has_permission(self, request, view):
        """
        Проверка прав доступа на уровне запроса.

        Аргументы:
        request (HttpRequest): Текущий HTTP запрос.
        view (APIView): Текущее представление.

        Возвращает:
        bool: True, если пользователь имеет доступ, иначе False.
        """
        return request.user.is_authenticated and request.user.is_admin
