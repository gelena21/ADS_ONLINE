from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny

from ads_online.filters import AdFilter
from ads_online.models import Ad, Review
from ads_online.paginations import AdPagination
from ads_online.permissions import IsOwnerOrAdmin
from ads_online.serializers import AdSerializer, ReviewSerializer


class AdListCreateView(generics.ListCreateAPIView):
    """
    Представление для отображения списка объявлений и создания нового объявления.

    Атрибуты:
    queryset (QuerySet): QuerySet для всех объявлений.
    serializer_class (Serializer): Класс сериализатора для модели Ad.
    permission_classes (list): Список классов разрешений.
    pagination_class (Pagination): Класс пагинации для объявлений.
    filter_backends (tuple): Кортеж классов фильтров.
    filter_class (FilterSet): Класс фильтра для модели Ad.
    """

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = AdFilter

    def perform_create(self, serializer):
        """
        Сохраняет новый объект объявления с автором текущего пользователя.

        Аргументы:
        serializer (Serializer): Сериализатор для модели Ad.
        """
        serializer.save(author=self.request.user)


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для отображения, обновления и удаления отдельного объявления.

    Атрибуты:
    queryset (QuerySet): QuerySet для всех объявлений.
    serializer_class (Serializer): Класс сериализатора для модели Ad.
    permission_classes (list): Список классов разрешений.
    """

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        """
        Обновляет объявление, проверяя права пользователя.

        Аргументы:
        serializer (Serializer): Сериализатор для модели Ad.

        Исключения:
        PermissionDenied: Если пользователь не автор объявления и не администратор.
        """
        if (
            self.request.user != serializer.instance.author
            and not self.request.user.is_staff
        ):
            raise PermissionDenied("У вас нет прав на внесение изменений")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Удаляет объявление, проверяя права пользователя.

        Аргументы:
        instance (Model): Экземпляр модели Ad.

        Исключения:
        PermissionDenied: Если пользователь не автор объявления и не администратор.
        """
        if self.request.user != instance.author and not self.request.user.is_staff:
            raise PermissionDenied("У вас нет прав на удаление")
        instance.delete()


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    Представление для отображения списка отзывов и создания нового отзыва.

    Атрибуты:
    queryset (QuerySet): QuerySet для всех отзывов.
    serializer_class (Serializer): Класс сериализатора для модели Review.
    permission_classes (list): Список классов разрешений.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self, serializer):
        """
        Сохраняет новый объект отзыва с автором текущего пользователя.

        Аргументы:
        serializer (Serializer): Сериализатор для модели Review.
        """
        serializer.save(author=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для отображения, обновления и удаления отдельного отзыва.

    Атрибуты:
    queryset (QuerySet): QuerySet для всех отзывов.
    serializer_class (Serializer): Класс сериализатора для модели Review.
    permission_classes (list): Список классов разрешений.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        """
        Обновляет отзыв, проверяя права пользователя.

        Аргументы:
        serializer (Serializer): Сериализатор для модели Review.

        Исключения:
        PermissionDenied: Если пользователь не автор отзыва и не администратор.
        """
        if (
            self.request.user != serializer.instance.author
            and not self.request.user.is_staff
        ):
            raise PermissionDenied("У вас нет прав на внесение изменений")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Удаляет отзыв, проверяя права пользователя.

        Аргументы:
        instance (Model): Экземпляр модели Review.

        Исключения:
        PermissionDenied: Если пользователь не автор отзыва и не администратор.
        """
        if self.request.user != instance.author and not self.request.user.is_staff:
            raise PermissionDenied("У вас нет прав на удаление")
        instance.delete()
