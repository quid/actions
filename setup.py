"""
setup.py

Setup for the actions package
"""
import os

from setuptools import find_packages
from setuptools import setup


try:
    import pypandoc
    long_description = pypandoc.convert("README.md", "rst")

except (IOError, ImportError):
    long_description = open("README.md").read()


setup(
    name="actions",
    version="1.0.2",
    description="Declarative actions",
    long_description=long_description,
    author="Quid Inc.",
    author_email="ops@quid.com",
    url="https://github.com/quid/actions",
    packages=find_packages(),
    install_requires=[
        "bunch==1.0.1"
    ]
)
