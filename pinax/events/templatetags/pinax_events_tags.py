from django import template
from django.utils import timezone

from ..models import Event


register = template.Library()


@register.simple_tag
def events():
    """
    Usage:
        {% events as var %}
    """
    return Event.objects.filter(published_at__lte=timezone.now()).order_by("-published_at")
