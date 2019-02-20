from django.apps import AppConfig


class ExampleConfig(AppConfig):
    name = 'socket_example'

    def ready(self):
        import socket_example.signals
