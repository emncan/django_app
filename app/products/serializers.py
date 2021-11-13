from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    """Serializer for product"""

    product_name = serializers.CharField(max_length=200)
    cat_id = serializers.CharField(max_length=200)
    stock = serializers.CharField(max_length=200)
    barcod = serializers.CharField(max_length=200)
    manufacturer = serializers.CharField(max_length=200)

    class Meta:
        model = Products
        fields = "__all__"
