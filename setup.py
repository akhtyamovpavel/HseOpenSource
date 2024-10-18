#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

ROOT_PACKAGE_NAME = 'triangle'


def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name=ROOT_PACKAGE_NAME,
    version='1.1',
    author=['Pavel Akhtyamov'],
    packages=find_packages(),
    long_description='triangles',
    requirements=parse_requirements()
)
