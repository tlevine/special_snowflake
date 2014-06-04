#!/usr/bin/env python3
from distutils.core import setup

setup(name='special_snowflake',
    author = 'Thomas Levine',
    author_email = '_@thomaslevine.com',
    description = 'Find the unique indices for a dataset',
    url = 'https://github.com/tlevine/special_snowflake.git',
    classifiers = [
        'Intended Audience :: Developers',
    ],
    packages = ['special_snowflake'],
    install_requires = ['sliding-window'],
    tests_require = ['nose'],
    version = '0.0.9',
    license = 'AGPL',
)
