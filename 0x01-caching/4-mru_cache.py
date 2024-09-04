#!/usr/bin/env python3

"""A class MRUCache that inherits from BaseCaching
 and is a caching system."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class that defines a basic caching algorithm
            using MRU (Least Recently Used)."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.data_order = []

    def put(self, key, item):
        """Add an item to the cache.

                        If the cache exceeds the MAX_ITEMS limit, the least
                         recently used item is discarded.
                        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.data_order.remove(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            deleted = self.data_order.pop(0)
            del self.cache_data[deleted]
            print(f"DISCARD: {deleted}")

        self.cache_data[key] = item
        self.data_order.insert(0, key)

    def get(self, key):
        """Retrieve an item from the cache by key.

                        Returns None if the key is not found or if the key is None.
                        """
        if key is None:
            return None
        try:
            data = self.cache_data[key]
            self.data_order.remove(key)
            self.data_order.insert(0, key)
            return data
        except KeyError:
            return None
