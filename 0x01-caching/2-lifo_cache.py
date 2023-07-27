#!/usr/bin/python3
"""A LIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        """initialize the function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """functions takes in key and item"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """function takes in key as argument"""
        for keys in key:
            if key == keys:
                return self.cache_data[key]
        return None
