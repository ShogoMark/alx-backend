#!/usr/bin/env python3
"""A caching module with class BasicCache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from parent class base_caching"""

    # function that assigns the item to the key
    def put(self, key, item):
        """takes in argument key and item"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    # function to retrieve the item of the key argument
    def get(self, key):
        """takes in argument key"""
        for keys in self.cache_data:
            if keys == key:
                return self.cache_data[key]
        return None
