#!/usr/bin/env python3

"""A class LFUCache that inherits from BaseCaching
 and is a caching system."""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class that defines a basic caching algorithm
            using LFU (Least Recently Used)."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.key_freq = {}
        self.freq_list = {}
        self.min_freq = 0

    def put(self, key, item):
        """Add an item to the cache.

                        If the cache exceeds the MAX_ITEMS limit, the least
                         recently used item is discarded.
                        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_key_frequency(key)

        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self._evict_least_frequently_used()

            self.cache_data[key] = item
            self.key_freq[key] = 1
            if 1 not in self.freq_list:
                self.freq_list[1] = []

            self.freq_list[1].append(key)
            self.min_freq = 1

    def get(self, key):
        """Retrieve an item from the cache by key.

                        Returns None if the key is not found or if the key is None.
                        """
        if key is None or key not in self.cache_data:
            return None

        self._update_key_frequency(key)
        return self.cache_data[key]

    def _update_key_frequency(self, key):
        """ a function to update the freq of key"""
        freq = self.key_freq[key]
        self.freq_list[freq].remove(key)
        # check if there is no lists with that frequency num
        if not self.freq_list[freq]:
            del self.freq_list[freq]
            # make sure updating min_freq
            if self.min_freq == freq:
                self.min_freq += 1

        new_freq = freq + 1
        self.key_freq[key] = new_freq
        if new_freq not in self.freq_list:
            self.freq_list[new_freq] = []
        self.freq_list[new_freq].append(key)

    def _evict_least_frequently_used(self):
        """ a function to evict the LFU item
        from the frames """
        keysOfMin = self.freq_list[self.min_freq]
        keyToEvict = keysOfMin.pop(0)

        if not keysOfMin:
            del self.freq_list[self.min_freq]

        del self.cache_data[keyToEvict]
        del self.key_freq[keyToEvict]
        print(f'DISCARD: {keyToEvict}')
