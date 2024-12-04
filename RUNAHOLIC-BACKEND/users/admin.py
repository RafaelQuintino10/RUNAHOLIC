# # users/admin.py
# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# User = get_user_model()

# # Registrando o modelo de usuário no admin
# admin.site.unregister(Group)
# admin.site.register(User)
from django.contrib import admin
from django.contrib.auth import get_user_model
from ecommerce.custom_admin import custom_admin_site

User = get_user_model()

# Personalizar o Django Admin para ocultar o app 'auth'
class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Filtrar a seção 'auth' do menu
        return [app for app in app_list if app['app_label'] != 'auth']

# Substituir o admin padrão
admin.site = CustomAdminSite(name='custom_admin')
# admin.site.register(User)
custom_admin_site.register(User)
