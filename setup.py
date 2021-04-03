#!/usr/bin/env python3
# -*- coding: utf-8 -*-from setuptools import setup
setup(
    name = 'fileListCreator',
    version = '0.1.0',
    packages = ['fileListCreator'],
    entry_points = {
        'console_scripts': [
            'fileListCreator = fileListCreator.__main__:main'
        ]
    })