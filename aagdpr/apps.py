"""
Config for the AA GDPR Django app.
"""

# Django
from django.apps import AppConfig

# AA GDPR
from aagdpr import __title__, __version__


class AagdprConfig(AppConfig):
    """
    Config for the AA GDPR Django app.
    """

    name = "aagdpr"
    label = "aagdpr"
    verbose_name = f"{__title__} v{__version__}"
