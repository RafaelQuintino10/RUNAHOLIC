from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Leitura para todos, criação para autenticados

    def get_permissions(self):
        # Apenas administradores podem criar, editar ou deletar produtos
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='category/(?P<category>\w+)')
    def by_category(self, request, category=None):
        """
        Retorna produtos filtrados por categoria.
        """
        filtered_products = Product.objects.filter(category=category)
        serializer = self.get_serializer(filtered_products, many=True)
        return Response(serializer.data)

# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Product, Category, Subcategory
# from .serializers import ProductSerializer, CategorySerializer, SubcategorySerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]  # Leitura para todos, criação para autenticados

#     def get_permissions(self):
#         # Apenas administradores podem criar, editar ou deletar produtos
#         if self.action in ['create', 'update', 'partial_update', 'destroy']:
#             self.permission_classes = [IsAdminUser]
#         else:
#             self.permission_classes = [IsAuthenticatedOrReadOnly]
#         return super().get_permissions()

#     @action(detail=False, methods=['get'], url_path='category/(?P<category>\w+)')
#     def by_category(self, request, category=None):
#         """
#         Retorna produtos filtrados por categoria.
#         """
#         try:
#             category_obj = Category.objects.get(name__iexact=category)
#         except Category.DoesNotExist:
#             return Response({"detail": "Categoria não encontrada."}, status=404)

#         filtered_products = Product.objects.filter(category=category_obj)
#         serializer = self.get_serializer(filtered_products, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=['get'], url_path='subcategory/(?P<subcategory>\w+)')
#     def by_subcategory(self, request, subcategory=None):
#         """
#         Retorna produtos filtrados por subcategoria.
#         """
#         try:
#             subcategory_obj = Subcategory.objects.get(name__iexact=subcategory)
#         except Subcategory.DoesNotExist:
#             return Response({"detail": "Subcategoria não encontrada."}, status=404)

#         filtered_products = Product.objects.filter(subcategory=subcategory_obj)
#         serializer = self.get_serializer(filtered_products, many=True)
#         return Response(serializer.data)


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAdminUser]  # Apenas administradores podem gerenciar categorias


# class SubcategoryViewSet(viewsets.ModelViewSet):
#     queryset = Subcategory.objects.all()
#     serializer_class = SubcategorySerializer
#     permission_classes = [IsAdminUser]  # Apenas administradores podem gerenciar subcategorias
