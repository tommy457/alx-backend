#!/usr/bin/env python3
"""
Module for the LFUCache class.
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ A class implementing a LFU cache replacement policy. """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.lfu_keys = {}

    def put(self, key, item):
        """ Add an item in the cache. """
        if key and item and self.cache_data.get(key) != item:

            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                k = min(self.lfu_keys, key=self.lfu_keys.get)
                self.cache_data.pop(k)
                self.lfu_keys.pop(k)
                print(f"DISCARD: {k}")

            self.lfu_keys[key] = self.lfu_keys.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key """
        if key in self.lfu_keys:
            self.lfu_keys[key] += 1
        return self.cache_data.get(key)
