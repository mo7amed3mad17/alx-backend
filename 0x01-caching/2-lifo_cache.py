#!/usr/bin/python3
""" LIFOCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOcaching class"""
    def __init__(self):
        """ Intialize cache"""
        super().__init__()
        self.last_key = None  # Track the last added key for LIFO eviction

    def put(self, key, item):
        """ Add an item to the cache using LIFO eviction policy """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # Add or update the item in the cache
        self.cache_data[key] = item

        # Check if we need to discard an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LIFO: Remove the most recently added
            if self.last_key is not None and self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

        # Update the last key to the current key
        self.last_key = key

    def get(self, key):
        """ Get an item by key from the cache """
        return self.cache_data.get(key, None)
