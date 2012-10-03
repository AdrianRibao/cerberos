.. django-users documentation master file, created by
   sphinx-quickstart on Thu Jul 19 12:19:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

cerberos documentation
======================

Cerberos is a django app that takes care of failed logins.

Contents:

.. toctree::
   :maxdepth: 2

Installation
============

.. code::

    pip install cerberos

Add ``'cerberos'`` to ``INSTALLED_APPS``

Add the URLs to urls.py:

.. code::

    # Django users
    url(r'^cerberos/', include('cerberos.urls')),

Usage
=====

To enable cerberos the login view must be decorated with cerberos.decorators.watch_logins.

Example:

.. code::

    from django.contrib.auth.views import login

    # Login view
    url(r'^login/', watch_logins(login)),

When the user is locked, it renders the template cerberos/user-locked.html. You can override the template to show the users the information you want.
These parameters are passed to the template:

ip: The ip address of the user locked
failed_access: The FailedAccessAttempt instance

Settings
========

MAX_FAILED_LOGINS: The maximum number of failed logins before blocking the user.
MEMORY_FOR_FAILED_LOGINS: The number in seconds after the failed access attemps will be forgotten. If set to 0, the attempts won't be forgotten. Default = 0

Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

