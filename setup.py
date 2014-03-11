#!/usr/bin/env python3
from distutils.core import setup

import special_snowflake as s

setup(name='special_snowflake',
    author = 'Thomas Levine',
    author_email = '_@thomaslevine.com',
    description = 'Find the unique indices for a dataset',
    url = 'https://github.com/tlevine/special_snwoflake.git',
    classifiers = [
        'Intended Audience :: Developers',
    ],
    packages = ['special_snowflake'],
    install_requires = ['sliding_window'],
    tests_require = ['nose'],
    version = s.__version__,
    license = 'AGPL',
)
