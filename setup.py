# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import multilogger
version = multilogger.__version__

setup(
    name='multilogger',
    version=version,
    author='Carlos de las Heras',
    author_email='cahersan@gmail.com',
    packages=[
        'multilogger',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['multilogger/manage.py'],
)
