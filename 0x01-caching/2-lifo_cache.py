#!/usr/bin/env python3
"""
Module for the LIFOCache class.
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ defines a LIFO Cache replacement policie."""
    def __init__(self):
        """ constructor """
        super().__init__()
        self.last_in = None

    def put(self, key, item):
        """ Add an item in the cache. """
        if key and item and self.cache_data.get(key) != item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(self.last_in)
                print(f"DISCARD {self.last_in}")
            self.last_in = key

    def get(self, key):
        """ Get an item by key. """
        return self.cache_data.get(key)
