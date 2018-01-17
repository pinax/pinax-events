from setuptools import find_packages, setup

VERSION = "2.0.3"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-events.svg
    :target: https://pypi.python.org/pypi/pinax-events/

============
Pinax Events
============

.. image:: https://img.shields.io/pypi/v/pinax-events.svg
    :target: https://pypi.python.org/pypi/pinax-events/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-events.svg
    :target: https://circleci.com/gh/pinax/pinax-events
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-events.svg
    :target: https://codecov.io/gh/pinax/pinax-events
.. image:: https://img.shields.io/github/contributors/pinax/pinax-events.svg
    :target: https://github.com/pinax/pinax-events/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-events.svg
    :target: https://github.com/pinax/pinax-events/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-events.svg
    :target: https://github.com/pinax/pinax-events/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-events/

\ 

``pinax-events`` is a simple app for publishing events on your site. 


Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
| 1.11            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
| 2.0             |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a simple app for publishing events on your site",
    name="pinax-events",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-events/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "events": []
    },
    test_suite="runtests.runtests",
    tests_require=[
        "Pillow"
    ],
    install_requires=[
        "django>=1.11",
        "django-imagekit>=3.3",
        "Markdown>=2.6.6",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)