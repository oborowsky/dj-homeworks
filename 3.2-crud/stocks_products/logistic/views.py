from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации
    filterset_fields = ['id', 'title', 'description']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'title', 'description']
    ordering_fields = ['id', 'title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации
    filterset_fields = ['products']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['products__title', 'products__description']
    ordering_fields = ['products__title', 'products__description']
