from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Nome do Produto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= 'Preço')
    description = models.TextField(blank=True, verbose_name= 'Descrição')
    #stock = models.IntegerField(default=0)
    CATEGORY_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('acessórios', 'Acessórios'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name= 'Categoria')
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Campo para imagem


    class Meta:
        verbose_name = 'Produto'
    

    def __str__(self):
        return self.name

# from django.db import models
# from django.core.exceptions import ValidationError

# class Category(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Categoria")

#     def __str__(self):
#         return self.name

# class Subcategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name="Categoria")
#     name = models.CharField(max_length=100, verbose_name="Subcategoria")

#     def __str__(self):
#         return f"{self.category.name} - {self.name}"

# class Product(models.Model):
#     name = models.CharField(max_length=200, verbose_name="Nome do Produto")
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
#     description = models.TextField(verbose_name="Descrição")
#     category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoria")
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Subcategoria")
#     stock = models.PositiveIntegerField(default=0,verbose_name="Estoque")

#     def clean(self):
#         if self.subcategory and self.subcategory.category != self.category:
#             raise ValidationError("A subcategoria deve pertencer à categoria selecionada.")
        
#     def __str__(self):
#         return self.name

