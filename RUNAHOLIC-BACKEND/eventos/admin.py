from django.contrib import admin

from django.contrib import admin
from .models import Evento
from ecommerce.custom_admin import custom_admin_site

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'preco_ingresso', 'quantidade_ingresso', 'data_evento', 'hora_evento')  
    search_fields = ('nome_evento',)  
    list_filter = ('nome_evento', 'quantidade_ingresso', 'data_evento')  

# Registra o modelo Product com as personalizações
# admin.site.register(Order, OrderAdmin)
custom_admin_site.register(Evento,EventoAdmin)