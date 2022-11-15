from django.db import models
from product.models import Orders

# Create your models here.

class Payment(models.Model):
    order = models.ForeignKey(Orders , on_delete = models.CASCADE , null = True)
    order_reg_id = models.CharField(max_length=50 , default=None , null=True)
    currency = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=50 , default=None , null=True)
    status = models.CharField(default='Pending' , max_length=30)
    