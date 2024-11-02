from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="1.0.0",
    author="Nick Rupprecht",
    author_email="nick.rupprecht@fau.de",
    description='math quiz for dsss homework',
    packages=find_packages(),
    install_requires=["random"],
)