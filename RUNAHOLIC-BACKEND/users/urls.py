# users/urls.py
from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-register'),  # Endpoint para registro
    path('profile/', UserDetailView.as_view(), name='user-detail'),     # Endpoint para visualizar o perfil do usuário autenticado
]
