from django.apps import AppConfig


class LedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'led'

    def ready(self):
        from . import mqtt
        mqtt.client.loop_start()
