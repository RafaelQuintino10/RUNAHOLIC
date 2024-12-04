# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import Evento
# from .serializers import EventoSerializer

# class EventoViewSet(viewsets.ModelViewSet):
#     queryset = Evento.objects.all()
#     serializer_class = EventoSerializer

from rest_framework import viewsets, permissions
from .models import Evento
from .serializers import EventoSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permissão personalizada que permite apenas leitura para todos e escrita apenas para administradores.
    """
    def has_permission(self, request, view):
        # Permitir acesso de leitura para todos (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Apenas administradores podem criar, editar ou deletar
        return request.user and request.user.is_staff

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAdminOrReadOnly]
