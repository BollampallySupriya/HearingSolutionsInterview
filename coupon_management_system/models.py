from django.db import models


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'coupon'
