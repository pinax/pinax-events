from django.apps import AppConfig as BaseAppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from imagekit import register

from .utils import load_path_attr


class AppConfig(BaseAppConfig):

    name = "pinax.events"
    label = "pinax_events"
    verbose_name = _("Pinax Events")

    def ready(self):
        image_path = getattr(
            settings,
            "PINAX_EVENTS_IMAGE_THUMBNAIL_SPEC",
            "pinax.events.specs.ImageThumbnail"
        )
        secondary_image_path = getattr(
            settings,
            "PINAX_EVENTS_SECONDARY_IMAGE_THUMBNAIL_SPEC",
            "pinax.events.specs.SecondaryImageThumbnail"
        )

        image_spec_class = load_path_attr(image_path)
        secondary_image_spec_class = load_path_attr(secondary_image_path)

        register.generator("pinax_events:image:thumb", image_spec_class)
        register.generator("pinax_events:secondary_image:thumb", secondary_image_spec_class)
