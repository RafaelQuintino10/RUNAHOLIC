from django.contrib import admin
from .models import Order
from ecommerce.custom_admin import custom_admin_site

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product','quantity','date')  
    search_fields = ('user', 'product')  
    list_filter = ('product', 'date', 'user')  

# Registra o modelo Product com as personalizações
# admin.site.register(Order, OrderAdmin)
custom_admin_site.register(Order,OrderAdmin)