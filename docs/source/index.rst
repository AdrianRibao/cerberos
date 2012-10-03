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

Settings
========

MAX_FAILED_LOGINS: The maximum number of failed logins before blocking the user.

Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

