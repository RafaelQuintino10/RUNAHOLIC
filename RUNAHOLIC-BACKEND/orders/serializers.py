# # orders/serializers.py
# from rest_framework import serializers
# from .models import Order

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

from rest_framework import serializers
from .models import Order
from django.contrib.auth import get_user_model

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)  # Adiciona o nome do produto
    product_price = serializers.DecimalField(source='product.price', read_only=True,max_digits=10, decimal_places=2)
    product_image = serializers.ImageField(source='product.imagem', read_only=True)  # Imagem do produto

    class Meta:
        model = Order
        fields = ['id','product','product_price','product_name', 'quantity', 'order_date', 'product_image']  # Não precisa incluir 'user' e 'order_date'
        read_only_fields = ['user']  # Garante que esses campos não sejam enviados

    def create(self, validated_data):
        # O campo 'user' é atribuído automaticamente ao usuário autenticado
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
