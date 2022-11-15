from django.urls import path
from .views import AllPayments , PaymentById , CreateTransaction

urlpatterns =[
    path('' , AllPayments),
    path('<int:id>', PaymentById),
    path('transaction/<int:id>', CreateTransaction)
] 
