import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.events"
    label = "pinax_events"
    verbose_name = _("Pinax Events")
