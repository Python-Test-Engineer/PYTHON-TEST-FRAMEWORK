"""setup.py to be able to do sibling imports - run pip install -e . in root"""

from setuptools import find_packages, setup

setup(name="iws", version="1.0.0", packages=find_packages())
