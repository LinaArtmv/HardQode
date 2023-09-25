from django.urls import path, re_path
from .views import (LessonViewSet, ProductLessonViewSet,
                    ProductsStatisticViewSet)


urlpatterns = [
    path('lessons/', LessonViewSet.as_view({'get': 'list'})),
    re_path(r'^products/(?P<product_id>\d+)/lessons/$',
            ProductLessonViewSet.as_view({'get': 'list'})),
    path('products/statistic/',
         ProductsStatisticViewSet.as_view({'get': 'list'}))
]
