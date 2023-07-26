#!/usr/bin/env python3
"""A FIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """functions takes in key and item"""
        if key is None or item is None:
            pass

        if len(self.cache_data) >= self.MAX_ITEMS:
            old_key = next(iter(self.cache_data))
            del self.cache_data[old_key]
            print("DISCARD: {}".format(old_key))

        self.cache_data[key] = item

    def get(self, key):
        """function takes in key as argument"""
        for keys in self.cache_data:
            if key == keys:
                return self.cache_data[key]
        return None
