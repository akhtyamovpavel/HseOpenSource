#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from glob import glob

import os
from pybind11.setup_helpers import Pybind11Extension, build_ext
ROOT_PACKAGE_NAME = 'triangle-hse-opensource'



ext_modules = [
    Pybind11Extension(
        "cpp_extension",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
    ),
]

setup(
    name=ROOT_PACKAGE_NAME,
    version='1.3',
    author='Pavel Akhtyamov',
    author_email='akhtyamovpavel@gmail.com',
    packages=['triangle'],
    description='Package of computing for HSE Open Source',
    #find_packages(
    #    include='triangle',
    #    exclude='test*',
    #),
    long_description='Package for computing triangle sum',
    install_requires=['six', 'pybind11'],
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules
)

