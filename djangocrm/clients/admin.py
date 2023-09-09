from django.contrib import admin
from clients.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'description', 'worker')
    fields = ('name', 'phone', 'email', 'description', 'worker', 'data', 'user')
    search_fields = ('name',)
    readonly_fields = ('data', 'user')


