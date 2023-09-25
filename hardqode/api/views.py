from rest_framework import viewsets
from .serializers import (LessonSerializer, ProductLessonSerializer,
                          ProductsStatisticSerializer)
from product.models import Review, Product


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """Выводит список всех уроков по всем продуктам,
    к которым пользователь имеет доступ."""

    serializer_class = LessonSerializer

    def get_queryset(self):
        return Review.objects.filter(
            product__access__user=self.request.user)


class ProductLessonViewSet(viewsets.ReadOnlyModelViewSet):
    """Выводит список уроков по конкретному продукту,
    к которому пользователь имеет доступ."""

    serializer_class = ProductLessonSerializer

    def get_queryset(self):
        return Review.objects.filter(
            product__access__user=self.request.user,
            product=self.kwargs.get('product_id'))


class ProductsStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    """Выводит статистику по продуктам."""

    serializer_class = ProductsStatisticSerializer
    queryset = Product.objects.all()
