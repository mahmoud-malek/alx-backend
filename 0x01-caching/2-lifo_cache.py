#!/usr/bin/env python3

""" a class FIFOCache that inherits
from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ a class that defines a basic
    caching algorithm """

    def __init__(self):
        """ initiative function that inherits from
        base """
        super().__init__()
        self.data_order = []

    def put(self, key, item):
        """ a function to put the value in
        the caching system """
        if key is None or item is None:
            return

        if (len(self.cache_data) >= self.MAX_ITEMS):
            deleted = self.data_order.pop()
            del self.cache_data[deleted]
            print(f"DISCARD: {deleted}")

        self.cache_data[key] = item
        self.data_order.append(key)

    def get(self, key):
        """ a function to get the cache value """
        if key is None:
            None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
