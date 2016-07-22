import pkg_resources


default_app_config = "pinax.events.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-events").version
