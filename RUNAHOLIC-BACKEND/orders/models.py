# orders/models.py
from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produto')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    quantity = models.PositiveIntegerField(verbose_name='Quantidade')
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pedido'
        

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
