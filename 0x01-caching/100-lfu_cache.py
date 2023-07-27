#!/usr/bin/python3
"""A LFUCache that inherits from BaseCaching"""

import heapq
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """class inherits from BaseCaching"""
    def __init__(self):
        """initialize the function"""
        super().__init__()
        self.freq_counter = defaultdict(int)
        self.freq_heap = []

    def put(self, key, item):
        """functions takes in key and item"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # update the item's value in the cache
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # if cache is full, delete the least frequent used item
                while self.freq_heap:
                    freq, lfu_key = heapq.heappop(self.freq_heap)
                    if self.freq_counter[lfu_key] == freq:
                        del self.cache_data[lfu_key]
                        del self.freq_counter[lfu_key]
                        break

        # add the new item to the cache with frequency 1
        self.cache_data[key] = item
        self.freq_counter[key] = 1
        heapq.heappush(self.freq_heap, (1, key))

    def get(self, key):
        """function takes in key as argument"""
        if key is None or key not in self.cache_data:
            return None

        self.freq_counter[key] += 1
        # update the frequency of the key in the freq heap
        heapq.heappush(self.freq_heap, (self.freq_counter[key], key))

        return self.cache_data[key]
