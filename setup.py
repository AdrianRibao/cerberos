#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from setuptools import setup, find_packages


version = '0.1.0'


if sys.argv[-1] == 'publish':
    subprocess.call(['python', 'setup.py', 'sdist', 'upload'])
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'Tag version %s'" % (version, version)
    print "  git push --tags"
    sys.exit()


setup(
    name='cerberos',
    version=version,
    description='',
    author='Adrián Ribao',
    url='',
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data = True,
    license='BSD',
)