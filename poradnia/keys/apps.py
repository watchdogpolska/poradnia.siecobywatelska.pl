from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomAppConfig(AppConfig):
    name = "poradnia.keys"
    verbose_name = _("Keys")
