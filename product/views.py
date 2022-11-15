
from rest_framework.decorators import api_view , permission_classes

from  rest_framework import  status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from .serializer import OrderSerializer, ProductsSerializer , OrderCreateSerializer
from .models import Products, ProductOptions, Orders

@api_view(['GET'])
@permission_classes([AllowAny])
def AllProducts(request):
    try:
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'result' : 'No Products to Show'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def ProductById(request , id):
    try:
        product = Products.objects.get(id=id)
        serializer = ProductsSerializer(product)
        return  Response({"result" : serializer.data} , status=status.HTTP_200_OK)
    except:
        return Response({'result' : 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def CreateProduct(request):
    product=ProductsSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response({"result":product.data},status=status.HTTP_200_OK)
    return Response({"error":product.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def AllOrders(request):
    try:
        queryset = Orders.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'result' : 'No Orders to Show'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def OrderById(request , id):
    try:
        order = Orders.objects.get(id=id)
        serializer = OrderSerializer(order)
        return  Response({"result" : serializer.data} , status=status.HTTP_200_OK)
    except:
        return Response({'result' : 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def CreateOrder(request):
    order = OrderCreateSerializer(data=request.data)
    if order.is_valid():
        order.save()
        return Response({"result":order.data},status=status.HTTP_200_OK)
    return Response({"error":order.errors},status=status.HTTP_400_BAD_REQUEST) 