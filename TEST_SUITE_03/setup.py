"""setup.py to be able to do sibling imports - run spip install -e . in root"""

from setuptools import setup, find_packages

setup(name="iws", version="1.0.0", packages=find_packages())
