#!/usr/bin/env python3
"""
Module for the MRUCache class.
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ defines a LRU Cache replacement policie. """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.mru_list = []

    def put(self, key, item):
        """ Add an item in the cache. """
        if key and item and self.cache_data.get(key) != item:
            if not (key in self.mru_list):
                self.mru_list.insert(1, key)

            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(self.mru_list[0])
                k = self.mru_list.pop(0)
                print(f"DISCARD: {k}")

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.mru_list.remove(key)
            self.mru_list.insert(0, key)

        return self.cache_data.get(key)
