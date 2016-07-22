from django.db import models
from django.utils import timezone

import markdown


class Event(models.Model):

    image = models.ImageField(upload_to="event-images", blank=True)
    title = models.CharField(max_length=200)
    url = models.TextField(blank=True)
    where = models.CharField(max_length=200)
    what = models.TextField()
    what_html = models.TextField(blank=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

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
