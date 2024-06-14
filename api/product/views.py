
from .decorators import customer_only
from rest_framework import viewsets, filters
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from .mixins import PlatformApiCallMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class OrderViewSet(PlatformApiCallMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['products__name']
    ordering_fields = ['amount']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @customer_only
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @customer_only
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Order.objects.all()
        elif hasattr(user, 'customer'):
            queryset = Order.objects.filter(customer__user=user).select_related(
                'customer', 'seller').prefetch_related('products')
        else:
            queryset = Order.objects.none()

        ordering = self.request.query_params.get('ordering', None)
        if ordering in self.ordering_fields:
            queryset = queryset.order_by(ordering)
        elif ordering == '-amount':
            queryset = queryset.order_by(
                '-amount')[:5]
        return queryset


class ProductViewSet(PlatformApiCallMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['products__name']
    ordering_fields = ['amount']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
