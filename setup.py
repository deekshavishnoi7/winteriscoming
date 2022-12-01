from distutils.core import setup
from setuptools import find_packages

setup(
    name="DSSS Homework 5 - Snowflake",
    version="0.1",
    author="Deeksha",
    author_email="deeksha.vishnoi@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)