#!/usr/bin/env python3
"""A FIFOCache that inherits from BaseCaching"""

from base_caching import BaseCaching:


class FIFOCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        super().__init__()


    def put(self, key, item):
        """functions takes in key and item"""
        if key is None or item is None:
            return

        if len(self.cache_data) > self.MAX_ITEMS:
            if key not in self.cache_data:
                oldest_key = next(iter(self.cache_data)) # Get the oldest key
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))
            else:
                return self.cache_data
         

    def get(self, key):
        """function takes in key as argument"""
        if key == keys:
            return self.cache_data[key]
        return None
