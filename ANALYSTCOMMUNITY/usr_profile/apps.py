from django.apps import AppConfig


class UsrProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usr_profile'


    def ready(self):
        import usr_profile.signals