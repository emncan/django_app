from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductsSerializer
from rest_framework.views import APIView
from .models import Products


class ProductsView(APIView):
    """Manege product in the database"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Create new product"""
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        """Retrive the products"""
        items = Products.objects.all()
        serializer = ProductsSerializer(items, many=True)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def patch(self, request, id=None):
        """Update product based on id"""
        try:
            item = Products.objects.get(id=id)
            serializer = ProductsSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        except Products.DoesNotExist:
            return Response({"status": "error", "data": f"id => {id} does not exist"})

    def delete(self, request, id=None):
        """Delete product based on id"""
        item = get_object_or_404(Products, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
