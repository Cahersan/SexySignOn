# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

requirements = parse_requirements('requirements.txt')
reqs = [str(r.req) for r in requirements]

setup(
    name='multilogger',
    version="0.1.0",
    author='Carlos de las Heras',
    author_email='cahersan@gmail.com',
    url='https://github.com/cahersan/multilogger',
    description='Login app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    zip_safe=False,
    scripts=['multilogger/manage.py'],
)
