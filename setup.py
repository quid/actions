"""
setup.py

Setup for the actions package
"""
import os

from setuptools import find_packages
from setuptools import setup


setup(
    name="actions",
    version="1.0.1",
    description="Declarative actions",
    author="Robert Roose",
    author_email="robert@shivercube.com",
    url="https://bitbucket.org/summatix/actions",
    packages=find_packages(),
    install_requires=[
        "bunch==1.0.1"
    ]
)
