# products/admin.py

from django.contrib import admin
from .models import Product
from ecommerce.custom_admin import custom_admin_site


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'imagem')  # Exibir esses campos na lista de produtos
    search_fields = ('name',)  # Permitir pesquisa pelo nome do produto
    list_filter = ('price', 'category')  # Filtrar produtos pelo preço

# Registra o modelo Product com as personalizações
# admin.site.register(Product, ProductAdmin)
custom_admin_site.register(Product, ProductAdmin)


# from django.contrib import admin
# from .models import Category, Subcategory, Product

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)

# @admin.register(Subcategory)
# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'category')
#     list_filter = ('category',)
#     search_fields = ('name',)
#     autocomplete_fields = ('category',)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'category', 'subcategory')
#     list_filter = ('price', 'category', 'subcategory')
#     search_fields = ('name', 'category__name', 'subcategory__name')
#     autocomplete_fields = ('category', 'subcategory')  # Campos de autocomplete para categorias e subcategorias
