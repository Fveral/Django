from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    # Campos a mostrar en el listado tupla
    readonly_fields = ('created', 'updated')
admin.site.register(Service, ServiceAdmin)