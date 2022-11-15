from django.urls import path
from .views import AllPayments , PaymentById , CreateTransaction , callback

urlpatterns =[
    path('' , AllPayments),
    path('<int:id>', PaymentById),
    path('transaction/<int:id>', CreateTransaction),
    path('callback/<int:id>',callback)
] 
