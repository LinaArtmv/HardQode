from rest_framework import serializers
from product.models import Review, Product, User
from django.db.models import Sum


class LessonSerializer(serializers.ModelSerializer):
    """Связан с эндпоинтом api/lessons/."""

    lesson = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('lesson', 'length', 'status')


class ProductLessonSerializer(serializers.ModelSerializer):
    """Связан с эндпоинтом api/product/product_id/lessons/."""

    lesson = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('lesson', 'length', 'status', 'date')


class ProductsStatisticSerializer(serializers.ModelSerializer):
    """Связан с эндпоинтом api/products/statistic/."""

    count_lesson = serializers.SerializerMethodField()
    summ_length = serializers.SerializerMethodField()
    count_user = serializers.SerializerMethodField()
    product_purchases = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'count_lesson',
                  'summ_length', 'count_user', 'product_purchases')

    def get_count_lesson(self, obj):
        return obj.reviews.filter(product=obj, status='Просмотрено').count()

    def get_summ_length(self, obj):
        return obj.reviews.filter(
            product=obj).aggregate(Sum('length'))['length__sum']

    def get_count_user(self, obj):
        return obj.access.count()

    def get_product_purchases(self, obj):
        count_product_user = self.get_count_user(obj)
        count_user = User.objects.count()
        return (count_product_user / count_user) * 100
