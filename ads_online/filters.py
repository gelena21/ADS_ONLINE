import django_filters
from .models import Ad

"""
    Фильтр для модели Ad, позволяющий искать объявления по названию.
    """


class AdFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        """
        Метакласс для определения модели и полей, которые будут использоваться в фильтре.
        """
        model = Ad
        fields = ['title']
