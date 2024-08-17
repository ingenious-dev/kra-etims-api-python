#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup module """

from setuptools import setup
import os
import re


# Get version from __init__.py file
VERSION = ""
with open("kra_etims/__init__.py", "r") as fd:
    VERSION = re.search(r"^__version__\s*=\s*['\"]([^\"]*)['\"]", fd.read(), re.MULTILINE).group(1)

if not VERSION:
    raise RuntimeError("Cannot find version information")

# Get long description
README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    # name="KRA eTIMS", # This will result in packa
    name="kra-etims",
    version=VERSION,
    description="A Python wrapper for the KRA eTIMS REST API",
    long_description=README,
    author="Joseph Suhudu @ ingenious.or.ke",
    author_email="suhudu+joseph@gmail.com",
    url="https://github.com/ingenious-dev/kra-etims-api-python",
    license="MIT License",
    packages=[
        "kra_etims"
    ],
    include_package_data=True,
    platforms=['any'],
    install_requires=[
        "requests"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='kra etims rest api',
    project_urls={
        'Source': 'https://github.com/ingenious-dev/kra-etims-api-python',
        'Tracker': 'https://github.com/ingenious-dev/kra-etims-api-python/issues',
    },
)
