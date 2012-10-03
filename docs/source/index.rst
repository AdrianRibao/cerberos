.. django-users documentation master file, created by
   sphinx-quickstart on Thu Jul 19 12:19:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cerberos documentation
======================

Cerberos is a django app that watches failed logins and block the user after N attempts.

When a user have tried to login a certain number of times, cerberos blocks the login view to the user.

Installation
============

Intallation is very simple:

.. code::

    pip install cerberos

After that, add ``'cerberos'`` to ``INSTALLED_APPS``

and run the migrations:

.. code::

    python manage.py migrate cerberos

Usage
=====

To enable cerberos the login view must be decorated with ``cerberos.decorators.watch_logins``.

Example:

.. code::

    from django.contrib.auth.views import login

    # Login view
    url(r'^login/', watch_logins(login)),

When the user is locked, it renders the template ``cerberos/user-locked.html``. You can override the template to show the users the information you want.

These parameters are passed to the template:

* **ip**: The ip address of the user locked
* **failed_access**: The ``FailedAccessAttempt`` instance

Settings
========

*MAX_FAILED_LOGINS:* The maximum number of failed logins before blocking the user.

*MEMORY_FOR_FAILED_LOGINS:* The number in seconds after the failed access attemps will be forgotten. If set to 0, the attempts won't be forgotten. Default = 0

CONTRIBUTE
==========

Cerberos is hosted at github: https://github.com/AdrianRibao/cerberos

Feel free to send us your comments, ideas and pull request.
