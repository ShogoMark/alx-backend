#!/usr/bin/python3
"""A LIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        """initialize the function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """functions takes in key and item"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # if key is already present, moves it to end(MRU)
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_used_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", least_used_key)
        self.cache_data[key] = item

    def get(self, key):
        """function takes in key as argument"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
