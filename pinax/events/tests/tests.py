from datetime import timedelta

from django.utils import timezone
from django.test import TestCase

from pinax.events.models import Event
from pinax.events.templatetags.pinax_events_tags import events


class Tests(TestCase):

    def test_html_generated_on_save(self):
        event = Event.objects.create(
            title="Test Event",
            where="Nashville, TN",
            what="### The Main Event\n\n* Item Number 1\n* Item Number 2",
            start_date=timezone.now().date(),
            end_date=timezone.now().date()
        )
        self.assertEquals(event.what_html, "<h3>The Main Event</h3>\n<ul>\n<li>Item Number 1</li>\n<li>Item Number 2</li>\n</ul>")

    def test_upcoming(self):
        start = timezone.now().date()
        end = (timezone.now() + timedelta(days=5)).date()
        Event.objects.create(
            title="Test Event",
            where="Nashville, TN",
            what="### The Main Event\n\n* Item Number 1\n* Item Number 2",
            start_date=start,
            end_date=end
        )
        self.assertEquals(Event.upcoming().count(), 1)

    def test_events_tag(self):
        start = timezone.now().date()
        end = (timezone.now() + timedelta(days=5)).date()
        Event.objects.create(
            title="Test Event",
            where="Nashville, TN",
            what="### The Main Event\n\n* Item Number 1\n* Item Number 2",
            start_date=start,
            end_date=end
        )
        self.assertEquals(events().count(), 1)
