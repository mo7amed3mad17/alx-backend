#!/usr/bin/python3
""" BLRUCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        # List to track the order of key usage for LRU eviction
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU eviction policy """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If the key already exists,
        # remove it to update the usage order
        if key in self.cache_data:
            self.usage_order.remove(key)

        # Add or update the item in the cache
        self.cache_data[key] = item
        # Update the usage order by adding the key to the end
        self.usage_order.append(key)

        # Check if we need to discard an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LRU: Remove the least recently used item (first in usage_order)
            # Remove the first key from the list
            least_used_key = self.usage_order.pop(0)
            del self.cache_data[least_used_key]
            print("DISCARD:", least_used_key)

    def get(self, key):
        """ Get an item by key from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the usage order since this key was accessed
        self.usage_order.remove(key)
        self.usage_order.append(key)  # Move the key to
