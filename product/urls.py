
from django.urls import path
from .views import AllProducts , ProductById, CreateProduct, AllOrders, OrderById, CreateOrder

urlpatterns =[
    path('products' , AllProducts),
    path('products/<int:id>' , ProductById),
    path('product/create' , CreateProduct),
    path('orders' , AllOrders),
    path('orders/<int:id>' , OrderById),
    path('orders/create' , CreateOrder)
]