#!/usr/bin/python3
""" FIFOCaching module
"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOcaching class"""
    def __init__(self):
        """ Intialize cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ PUT method"""
        if key is not None and item is not None:
            self.queue.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

    def get(self, key):
        """ Get an item by key from the cache
        """
        return self.cache_data.get(key, None)
