from setuptools import find_packages
from setuptools import setup

setup(
    name='py_action_int',
    version='0.0.0',
    packages=find_packages(
        include=('py_action_int', 'py_action_int.*')),
)
