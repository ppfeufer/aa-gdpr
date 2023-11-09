from django.apps import AppConfig


class FlatlyThemeConfig(AppConfig):
    name = "aagdpr.theme.flatly"
    label = "flatly"
    version = "5.3.2"
    verbose_name = f"Bootswatch Flatly v{version}"

    def ready(self):
        pass
