from django.apps import AppConfig


class GroceryConfig(AppConfig):
    name = 'grocery'
    def ready(self):
        import grocery.mysignal
