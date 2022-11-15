
from rest_framework import serializers
from .models import Products , Orders , ProductOptions

class ProductOptionsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ProductOptions
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    options = ProductOptionsSerializer()
    class Meta:
        model = Products
        fields = '__all__'
        depth = 1
            
    def create(self, validated_data):
        print(validated_data)
        options = validated_data.pop('options')
        option=ProductOptions.objects.create(**options)
        
        new_product = Products.objects.create(options=option , **validated_data)
        new_product.save()
        
        return new_product
    


class OrderSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)
    
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1
        
class OrderCreateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True , queryset=Products.objects.all())
    totalPrice = serializers.SerializerMethodField()
    totalPrice = 0
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1
        
        
    def get_totalPrice(self , instance):
        price = instance.options.price
        self.totalPrice += price
        return self.totalPrice
        
        
    def create(self, validated_data):
        print(validated_data)
        total = 0
        products = validated_data.pop('products' , None)
        
        for product in products:
            total = self.get_totalPrice(product)
            
        order = Orders.objects.create(total_price=total,  **validated_data)
        if products:
            order.products.set(products)

        return order
    
        
