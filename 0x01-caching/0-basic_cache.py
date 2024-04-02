#!/usr/bin/env python3
"""
Module for the BasicCache class.
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ class for basic caching system. """

    def __init__(self):
        """ constractur """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache. """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
