from rest_framework.pagination import PageNumberPagination


class AdPagination(PageNumberPagination):
    """
    Класс для пагинации объявлений.

    Атрибуты:
    page_size (int): Количество объектов на странице.
    page_size_query_param (str): Параметр запроса для указания количества объектов на странице.
    max_page_size (int): Максимальное количество объектов на странице.
    """
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4
