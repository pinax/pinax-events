# pinax-events


!!! note "Pinax Ecosystem"
    This app is part of the Pinax ecosystem and is designed for use
    both with and independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

To install pinax-events:

    pip install pinax-events

Add `pinax-events` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = (
        ...
        "imagekit",
        "pinax.events",
        ...
    )
```

You will need either `PIL` or `Pillow` installed for `imagekit` to work.  We
recommend `Pillow`:

    pip install Pillow


## Settings

There are two settings that have defaults but if you want to override them you
need to just set them to the dotted-notation path to the `ImageSpec` class that
you wish to use to process the `image` and `secondary_image` files for the
`image_thumb` and `secondary_image_thumb` attributes on the `News` model.

```python
PINAX_EVENTS_IMAGE_THUMBNAIL_SPEC = "pinax.events.specs.ImageThumbnail"
PINAX_EVENTS_SECONDARY_IMAGE_THUMBNAIL_SPEC = "pinax.events.specs.SecondaryImageThumbnail"
```

To create your own `ImageSpec` classes you can reference the defaults, but it is
basically subclassing `imagekit.ImageSpec`.

## Usage

In your template where you want to display events:

First, load the template tags:

    {% load pinax_events_tags %}

Then:

    {% events as event_items %}

And here is an example that how you can show the events:

```html
    <section class="event-list">
        {% for event in event_items %}
            <article class="event" style="{% if event.secondary_image_thumb %}background-image:url({% static event.secondary_image_thumb.url %});{% endif %}">
                <section class="event-img">
                    <a href="{{ event.url }}">
                        {% if event.image_thumb %}<img src="{{ event.image_thumb.url }}" width="200" />{% endif %}
                    </a>
                </section>
                <ul class="event-details">
                    <li>
                        <h2><a href="{{ event.url }}">{{ event.title }}</a></h2>
                    </li>
                    <li class="meta">
                        <span>
                            Where: {{ event.where }}
                        </span>
                        <span>
                            When: {{ event.start_date }}&endash;{{ event.end_start }}
                        </span>
                    </li>
                    <li class="event-description">
                        {{ event.what_html|safe }}
                    </li>
                </ul>
            </article>
        {% endfor %}
    </section>
```

Add and manage events via the Django admin.

## Changelog

See [Changelog](./changelog.md).
