#!/usr/bin/env python3

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key == None or item == None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        for keys in self.cache_data:
            if keys == key:
                return self.cache_data[key]
        return None
