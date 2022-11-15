

from django.db import models

class ProductOptions(models.Model):
    color = models.CharField(max_length = 128)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    
    def __str__(self):
        return self.color

class Products(models.Model):
    name = models.CharField(max_length = 128)
    category = models.CharField(max_length = 128)
    options = models.OneToOneField(ProductOptions , on_delete = models.CASCADE , null = True)
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    client_name = models.CharField(max_length = 128)
    products = models.ManyToManyField(Products)
    total_price = models.DecimalField(max_digits=5 , decimal_places=2 , default= 0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.client_name


    
    

       

    


    

