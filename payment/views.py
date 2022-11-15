from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from helper.requests import *
from .serializer import PaymentSerializer
from product.serializer import OrderSerializer
from .models import Payment
from product.models import Orders


    
@api_view(['GET'])
@permission_classes([AllowAny])
def AllPayments(request):
    queryset = Payment.objects.all()
    if queryset:
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'result' : 'No Bills to Show'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def PaymentById(request,id):
    payment = Payment.objects.get(id=id)
    if payment :
        serializer = PaymentSerializer(payment)
        return  Response({"result" : serializer.data} , status=status.HTTP_200_OK)
    return Response({'result' : 'Bill not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def CreateTransaction(request , id):
    order_id = id
    payment = Payment.objects.get(order = order_id)
    order = Orders.objects.get(id=order_id)
    serializer = OrderSerializer(order)
    products = serializer.data['products']
    token = AuthenticationToken()
    order_reg_id = OrderRegistration(token=token , amount_cents=str(order.total_price* 100)  , items=[])
    payment.order_reg_id=order_reg_id
    payment.save()
    payment_token = GetPaymentKey(order_reg_id=order_reg_id , 
                                  token=token , 
                                  amount_cents=str(order.total_price * 100) , 
                                  currency=payment.currency , 
                                  client_name=order.client_name)
    Iframe_url = CreateIFrame(payment_token=payment_token)
    return Response({'result' : Iframe_url} , status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def callback(request):
    print(request.data)
    transaction_id = request.data['obj']['id']
    transaction_status = request.data['obj']['success']
    order_reg_id = request.data['obj']['order']['id']
    payment = Payment.objects.get(order_reg_id=order_reg_id)
    if transaction_status == True:
        payment.status = 'done'
        payment.transaction_id = transaction_id
        payment.save()
    
        serializer = PaymentSerializer(payment)
        data = serializer.data
        client_name = data['order']['client_name']
        total_price = data['order']['total_price']
        created = data['created']
        transaction_status = data['status']
        products = data['order']['products']
        
        message = """
        Hi , Mr {:s} , I hope you are fine,
        We want to confirm that your transaction was successful
        Bill Details:
        client_name : {:s}
        Total Price : {:s}
        created at : {:s}
        transaction status : {:s}
        Products : {}
        """.format(client_name,total_price,created,transaction_status , products)
        print(message)
        # HandleThreads('Payment Notification',
        #                 , 
        #                 ['ayaelkilany735@gmail.com']).start()
        return Response(status.HTTP_200_OK)
    else:
        payment.status = 'failed'
        payment.save()
        # HandleThreads( 'Notification',
        #               'This a confirmation message that your transaction has a problem and it was stopped' ,
        #               ['ayaelkilany735@gmail.com']).start()
        return Response(status.HTTP_400_BAD_REQUEST)
    
    
    