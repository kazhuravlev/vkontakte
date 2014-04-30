#!/usr/bin/env python
from distutils.core import setup

version='1.3.4'

setup(
    name='vkontakte2',
    version=version,
    author='Prosto Chewey',
    author_email='prosto.chewey@gmail.com',

    packages=['vkontakte'],

    url='https://github.com/prosto-chewey/vkontakte/',
    license = 'MIT license',
    description = 'vk.com (vkontakte.ru) API wrapper',

    long_description = open('README.rst').read() + open('CHANGES.rst').read(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
