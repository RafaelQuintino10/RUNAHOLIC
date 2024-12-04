from django.contrib.admin import AdminSite
from django.contrib import admin


class CustomAdminSite(AdminSite):
    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request, app_label)
        return app_list
custom_admin_site = CustomAdminSite(name='custom_admin')
