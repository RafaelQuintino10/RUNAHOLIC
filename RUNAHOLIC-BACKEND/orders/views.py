# orders/views.py
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.none()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Verifique se o usuário está autenticado
        user = self.request.user
        if user.is_authenticated:
            print(f"Usuário autenticado: {user.username}")
            serializer.save(user=user)
        else:
            print("Usuário não autenticado!")
            serializer.save(user=None)  # Isso é uma medida de segurança, não deveria ocorrer se o usuário for autenticado
