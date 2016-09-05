import uuid

from django.db import models
from django.utils import timezone

import markdown

from imagekit.models import ImageSpecField


def image_upload_to(instance, filename):
    uid = str(uuid.uuid4())
    ext = filename.split(".")[-1].lower()
    return "event-images/{}/{}.{}".format(instance.pk, uid, ext)


class Event(models.Model):

    image = models.ImageField(upload_to=image_upload_to, blank=True)
    secondary_image = models.ImageField(upload_to=image_upload_to, blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField(blank=True)
    where = models.CharField(max_length=200)
    what = models.TextField()
    what_html = models.TextField(blank=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    image_thumb = ImageSpecField(source="image", id="pinax_events:image:thumb")
    secondary_image_thumb = ImageSpecField(source="secondary_image", id="pinax_events:secondary_image:thumb")

    def save(self, *args, **kwargs):
        if self.what:
            self.what_html = markdown.markdown(self.what)
        return super(Event, self).save(*args, **kwargs)

    @classmethod
    def upcoming(cls):
        now = timezone.now()
        return cls.objects.filter(
            published_at__lte=now
        ).filter(
            end_date__gte=now.date()
        )
