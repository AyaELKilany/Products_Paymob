from django.contrib import admin
from .models import Products , ProductOptions , Orders
# Register your models here.

admin.site.register(Products)
admin.site.register(ProductOptions)
admin.site.register(Orders)
