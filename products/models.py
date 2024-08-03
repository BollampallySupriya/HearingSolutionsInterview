from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    quantity_in_stock = models.IntegerField()

    class Meta:
        db_table = "product"
