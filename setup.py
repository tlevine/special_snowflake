from distutils.core import setup

setup(name='special_snowflake',
    author='Thomas Levine',
    author_email='_@thomaslevine.com',
    description='Find the unique indices for a dataset',
    url='https://github.com/tlevine/special_snwoflake.git',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    packages=['special_snowflake'],
    install_requires = ['sliding_window'],
    tests_require = ['nose'],
    version='0.0.2',
    license='AGPL',
)
