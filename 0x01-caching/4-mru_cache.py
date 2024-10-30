#!/usr/bin/python3
""" MRUCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        # List to track the order of key usage for MRU eviction
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache using MRU eviction policy """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If the key already exists, update the cache and usage order
        if key in self.cache_data:
            # Remove the key to re-add it as most recent
            self.usage_order.remove(key)

        # Add or update the item in the cache
        self.cache_data[key] = item
        # Add key to the end as the most recently used
        self.usage_order.append(key)

        # Check if we need to discard an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # MRU: Remove the most recently used item (last in usage_order)
            # Get second-to-last item added
            most_recent_key = self.usage_order.pop(-2)
            del self.cache_data[most_recent_key]
            print("DISCARD:", most_recent_key)

    def get(self, key):
        """ Get an item by key from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order since this key was accessed
        self.usage_order.remove(key)
        # Move the key to the end to mark it as recently used
        self.usage_order.append(key)
        return self.cache_data[key]
