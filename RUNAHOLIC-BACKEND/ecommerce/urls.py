# ecommerce/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from orders.views import OrderViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from ecommerce.custom_admin import custom_admin_site
from eventos.views import EventoViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'eventos', EventoViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', custom_admin_site.urls),  # Usa o admin personalizado

    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),  # Para login/logout
    path('api/users/', include('users.urls')),  # Para registro e perfil do usuário
    path('api/token-auth/', obtain_auth_token)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
