from rest_framework import serializers

from ads_online.models import Ad, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at', 'reviews']

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews', None)
        ad = Ad.objects.create(**validated_data)
        if reviews_data:
            for review_data in reviews_data:
                Review.objects.create(ad=ad, **review_data)
        return ad
