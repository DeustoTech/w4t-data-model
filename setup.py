"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='w4t-data-model',
    version='0.83',
    description='A django model to manage Waste4Think waste collection data.',

    long_description=long_description,
    url='https://github.com/josubg/pyfiware',
    author='Josu Bermudez',
    author_email='josu.bermudez@deusto.es',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages=find_packages(),
    install_requires=['django-orion-model'],
)
