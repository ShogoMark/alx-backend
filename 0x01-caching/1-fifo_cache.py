#!/usr/bin/python3
"""A FIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        """initialize the function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """functions takes in key and item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """function takes in key as argument"""
        for keys in key:
            if key == keys:
                return self.cache_data[key]
        return None
