from django.db import models


class Products(models.Model):
    """Product object"""

    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    cat_id = models.CharField(max_length=255, blank=True, null=True)
    stock = models.CharField(max_length=255, blank=True, null=True)
    barcod = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "products"
