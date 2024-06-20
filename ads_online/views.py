from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination
from ads_online.filters import AdFilter
from ads_online.models import Ad, Review
from ads_online.permissions import IsOwnerOrAdmin
from ads_online.serializers import AdSerializer, ReviewSerializer


class AdPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class AdListCreateView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = AdFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author and not self.request.user.is_staff:
            raise PermissionDenied('У вас нет прав на вношение изменений')
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author and not self.request.user.is_staff:
            raise PermissionDenied('У вас нет прав на удаление')
        instance.delete()


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author and not self.request.user.is_staff:
            raise PermissionDenied('У вас нет прав на вношение изменений')
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author and not self.request.user.is_staff:
            raise PermissionDenied('У вас нет прав на удаление')
        instance.delete()
