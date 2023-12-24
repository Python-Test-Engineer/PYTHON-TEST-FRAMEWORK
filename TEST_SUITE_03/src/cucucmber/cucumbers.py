"""
This module contains a simple class modeling a cucumber basket.
Cucumbers may be added or removed from the basket.
The basket has a maximum size, however.
"""
# type:ignore


class CucumberBasket:
    """Doc"""

    def __init__(self, initial_count: int = 0, max_count: int = 10):
        if initial_count < 0:
            raise ValueError("Initial cucumber basket count must not be negative")
        if max_count < 0:
            raise ValueError("Max cucumber basket count must not be negative")

        self._count: int = initial_count
        self._max_count: int = max_count

    @property
    def count(self) -> int:
        """Doc"""
        return self._count

    @property
    def full(self) -> bool:
        """Doc"""
        return self.count == self._max_count

    @property
    def empty(self) -> bool:
        """Doc"""
        return self.count == 0

    @property
    def max_count(self) -> int:
        """Doc"""
        return self._max_count

    def add(self, count: int = 1) -> int:
        """Doc"""
        new_count = self.count + count
        if new_count > self.max_count:
            raise ValueError("Attempted to add too many cucumbers")
        self._count = new_count
        return self._count

    def remove(self, count: int = 1) -> int:
        """Doc"""
        new_count = self.count - count
        if new_count < 0:
            raise ValueError("Attempted to remove too many cucumbers")
        self._count = new_count
        return self._count
