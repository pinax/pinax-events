![](http://pinaxproject.com/pinax-design/patches/pinax-events.svg)

# Pinax Events

[![](https://img.shields.io/pypi/v/pinax-events.svg)](https://pypi.python.org/pypi/pinax-events/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-events.svg)](https://circleci.com/gh/pinax/pinax-events)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-events.svg)](https://codecov.io/gh/pinax/pinax-events)
[![](https://img.shields.io/github/contributors/pinax/pinax-events.svg)](https://github.com/pinax/pinax-events/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-events.svg)](https://github.com/pinax/pinax-events/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-events.svg)](https://github.com/pinax/pinax-events/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Settings](#settings)
  * [Usage](#usage)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## pinax-events

### Overview

``pinax-events`` is a simple app for publishing events on your site.

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

### Installation

To install pinax-events:

```commandline
    $ pip install pinax-events
```

Add `pinax-events` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "imagekit",
        "pinax.events",
    ]
```

You will need either `PIL` or `Pillow` installed for `imagekit` to work.  We
recommend `Pillow`:

```commandline
    $ pip install Pillow
```

### Settings

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

### Usage

In your template where you want to display events:

First, load the template tags:

```djangotemplate
    {% load pinax_events_tags %}
```

Then:

```djangotemplate
    {% events as event_items %}
```

And here is an example that how you can show the events:

```djangotemplate
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


## Change Log

### 2.0.3

* Add django>=1.11 to requirements
* Update CI config
* Remove doc build support
* Add sorting guidance for 3rd-party app imports
* Improve documentation markup

### 2.0.2

* fix setup.py LONG_DESCRIPTION for PyPi

### 2.0.1

* Fix setup.py for PyPi

### 2.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Move documentation into README
* Standardize documentation layout
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description

### 1.1.1

* added missing migrations from 1.1.0 changes

### 1.1.0

* added support for secondary images
* added support for customized image sizing

### 1.0.0

* added docs and tests and wired up CI

### 0.1

* initial release


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
