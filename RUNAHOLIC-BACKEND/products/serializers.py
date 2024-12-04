# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# from rest_framework import serializers
# from .models import Category, Subcategory, Product

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class SubcategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subcategory
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     category_name = serializers.ReadOnlyField(source='category.name')
#     subcategory_name = serializers.ReadOnlyField(source='subcategory.name')

#     class Meta:
#         model = Product
#         fields = '__all__'
