"""
setup.py

Setup for the actions package
"""
import os

from setuptools import find_packages
from setuptools import setup


requirements_txt = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "requirements.txt"
)
requires = []


with open(requirements_txt) as requirements:
    requires = requirements.read().split()


setup(
    name="actions",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requires
)