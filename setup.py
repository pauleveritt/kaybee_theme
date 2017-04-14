#!/usr/bin/env python

import codecs
from setuptools import setup

version = '0.0.1'

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='kaybee_theme',
    entry_points={
        'sphinx_themes': [
            'path = kaybee_theme:get_path',
        ]
    },
    version=version,
    description='Sphinx theme based on Bootstrap 4',
    long_description=readme,
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://github.com/pauleveritt/kaybee_theme',
    packages=['kaybee_theme'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
