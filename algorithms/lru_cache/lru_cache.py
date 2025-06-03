"""Simple LRU cache implementation."""
from __future__ import annotations

from collections import OrderedDict


class LRUCache:
    """Least Recently Used (LRU) cache."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._data: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int | None:
        if key not in self._data:
            return None
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key: int, value: int) -> None:
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)
