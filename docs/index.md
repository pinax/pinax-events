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
        "pinax.events",
        ...
    )
```

## Usage

In your template where you want to display events:

First, load the template tags:

    {% load pinax_events_tags %}

Then:

    {% events as event_items %}

And here is an example that how you can show the events:

    <section class="event-list">
        {% for event in event_items %}
            <article class="event">
                <section class="event-img">
                    <a href="{{ event.url }}">
                        <img src="{{ event.image.url }}" width="200" />
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

Add and manage events via the Django admin.

## Changelog

See [Changelog](./changelog.md).
