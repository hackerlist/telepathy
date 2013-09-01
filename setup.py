#-*- coding: utf-8 -*-

"""
    telepathy
    ~~~~~~~~~

    Setup
    `````

    $ pip install .
"""

from distutils.core import setup
import os

setup(
    name='telepathy',
    version='0.0.01',
    url='http://github.com/hackerlist/telepathy',
    author='mek',
    author_email='m@hackerlist.net',
    packages=[
        'telepathy',
        'telepathy/controllers',
        'telepathy/test',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'tornado',
        'PyMongo',
        'flup'
    ],
    description="A realtime environment on top of Tornado websockets for increasing transparency between users",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
