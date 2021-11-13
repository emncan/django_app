from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from products.serializers import ProductsSerializer
from rest_framework import filters, generics
from products.serializers import Products


class ProductsFilterView(generics.ListAPIView):
    """Simple equality-based product filtering"""

    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"


class ProductsOrderView(generics.ListAPIView):
    """Simple query parameter controlled ordering of results"""

    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = "__all__"


class ProductsSearchView(generics.ListAPIView):
    """Simple single query parameter based searching"""

    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["product_name", "manufacturer"]
