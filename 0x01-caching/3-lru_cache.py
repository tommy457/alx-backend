#!/usr/bin/env python3
"""
Module for the LIFOCache class.
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ defines a LRU Cache replacement policie. """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """ Add an item in the cache. """
        if key and item and self.cache_data.get(key) != item:
            if not (key in self.lru_list):
                self.lru_list.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(self.lru_list[0])
                k = self.lru_list.pop(0)
                print(f"DISCARD: {k}")

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.lru_list.remove(key)
            self.lru_list.append(key)

        return self.cache_data.get(key)
