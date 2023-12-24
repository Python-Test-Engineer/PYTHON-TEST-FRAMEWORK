"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework for testing classes.
"""


# --------------------------------------------------------------------------------
# Class: Accumulator
# --------------------------------------------------------------------------------


class Accumulator:
    """Doc"""

    def __init__(self):
        self._count = 0

    @property
    def count(self):
        """Doc"""
        return self._count

    def add(self, more: int = 1):
        """Doc"""
        self._count += more
