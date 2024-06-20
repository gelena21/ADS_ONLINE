from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AdListCreateView, AdDetailView, ReviewListCreateView, ReviewDetailView

app_name = 'ads_online'
router = DefaultRouter()

urlpatterns = [
    path('ads/', AdListCreateView.as_view(), name='ad-list'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
] + router.urls
