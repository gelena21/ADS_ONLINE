from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AdDetailView,
    AdListCreateView,
    ReviewDetailView,
    ReviewListCreateView,
)

app_name = "ads_online"
router = DefaultRouter()

urlpatterns = [
    path("ads/", AdListCreateView.as_view(), name="ad-list"),
    path("ads/<int:pk>/", AdDetailView.as_view(), name="ad-detail"),
    path("reviews/", ReviewListCreateView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
] + router.urls

"""
urlpatterns содержит маршруты для приложения ads_online.

Маршруты:
- 'ads/': Отображает список объявлений и позволяет создавать новые объявления.
- 'ads/<int:pk>/': Отображает подробности, обновляет или удаляет объявление по его ID.
- 'reviews/': Отображает список отзывов и позволяет создавать новые отзывы.
- 'reviews/<int:pk>/': Отображает подробности, обновляет или удаляет отзыв по его ID.
"""
