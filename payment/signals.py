from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Orders
from .models import Payment

@receiver(post_save , sender=Orders)
def createPayment(sender , instance , created, **kwargs):
    if created:
        total = 0
        payment = Payment.objects.create(order=instance , currency='EGP' , status='pending')
        payment.save()