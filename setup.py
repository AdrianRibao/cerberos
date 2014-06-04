#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


version = '0.2.1'

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)


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
    author_email='adrian@adrima.es',
    url='https://github.com/AdrianRibao/cerberos',
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data = True,
    license='BSD',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    install_requires=[
    ],
)
