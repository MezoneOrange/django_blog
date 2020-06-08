from django.apps import AppConfig


class RegConfig(AppConfig):
    name = 'reg'

    def ready(self):
        import reg.signals
