#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from setuptools import setup, find_packages


version = '0.2.0'


if sys.argv[-1] == 'publish':
    subprocess.call(['python', 'setup.py', 'sdist', 'upload'])
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'Tag version %s'" % (version, version)
    print "  git push --tags"
    sys.exit()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='cerberos',
    version=version,
    description='Cerberos is a django app that watches failed logins and block the user after N attempts.',
    author='Adrián Ribao',
    url='https://github.com/AdrianRibao/cerberos',
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data = True,
    license='BSD',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
    ],
)
