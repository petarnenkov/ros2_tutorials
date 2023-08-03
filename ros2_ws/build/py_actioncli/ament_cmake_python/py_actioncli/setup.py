from setuptools import find_packages
from setuptools import setup

setup(
    name='py_actioncli',
    version='0.0.0',
    packages=find_packages(
        include=('py_actioncli', 'py_actioncli.*')),
)
