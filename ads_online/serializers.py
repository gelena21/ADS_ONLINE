from rest_framework import serializers
from ads_online.models import Ad, Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Review.
    """

    class Meta:
        model = Review
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Ad, включающий связанные отзывы.
    """
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at', 'reviews']

    def get_reviews(self, obj):
        """
        Получает связанные отзывы для данного объявления.

        Аргументы:
        obj (Ad): Экземпляр модели Ad.

        Возвращает:
        list: Сериализованные данные отзывов.
        """
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data

    def create(self, validated_data):
        """
        Создает новое объявление вместе с отзывами.

        Аргументы:
        validated_data (dict): Проверенные данные для создания объявления.

        Возвращает:
        Ad: Созданный экземпляр модели Ad.
        """
        reviews_data = validated_data.pop('reviews', None)
        ad = Ad.objects.create(**validated_data)
        if reviews_data:
            for review_data in reviews_data:
                Review.objects.create(ad=ad, **review_data)
        return ad
