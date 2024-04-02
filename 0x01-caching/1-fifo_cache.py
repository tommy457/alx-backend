#!/usr/bin/env python3
"""
Module for the FIFOCache class.
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ class define a FIFO Cache replacement policie. """

    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache. """
        if key and item and self.cache_data.get(key) != item:
            self.cache_data[key] = item

            while len(self.cache_data) > self.MAX_ITEMS:
                k, _ = next(iter(self.cache_data.items()))
                del self.cache_data[k]
                print(f"DISCARD {k}")

    def get(self, key):
        """ Get an item by key. """
        return self.cache_data.get(key)
