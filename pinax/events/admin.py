from django.contrib import admin

from .models import Event


admin.site.register(Event, list_display=["title", "image", "where", "what", "start_date", "end_date", "published_at", "created_at"])
