from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    # cambiar el nombre del servicio en el panel de administración
    verbose_name = "Gestor de servicios"
