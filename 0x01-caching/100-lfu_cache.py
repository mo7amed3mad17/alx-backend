#!/usr/bin/python3
""" LFUCaching module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFU Cache system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        # Track access frequency of keys
        self.usage_frequency = defaultdict(int)
        # Track access order for LRU among least used
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using LFU eviction policy """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If key exists, update item and increase frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            # Move key to the end to mark it as recently used
            self.usage_order.move_to_end(key)
        else:
            # Add new item and track usage
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict LFU item if limit is exceeded
                self.evict_lfu_item()

            # Insert the new key with frequency 1 and item in cache
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order[key] = True  # Add key to the end for LRU order

    def get(self, key):
        """ Get an item by key from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and LRU order
        self.usage_frequency[key] += 1
        self.usage_order.move_to_end(key)  # Mark as recently used
        return self.cache_data[key]

    def evict_lfu_item(self):
        """ Evict the least frequently used item, using LRU if tied """
        # Find the minimum frequency among the items
        min_freq = min(self.usage_frequency.values())

        # Collect all items with the minimum frequency
        lfu_keys = \
            [k for k, freq in self.usage_frequency.items() if freq == min_freq]

        # Use LRU policy among keys with the lowest frequency
        lfu_key = lfu_keys[0]
        if len(lfu_keys) > 1:
            for k in self.usage_order:
                if k in lfu_keys:
                    lfu_key = k
                    break

        # Remove the LFU (and LRU among ties) key from all records
        del self.cache_data[lfu_key]
        del self.usage_frequency[lfu_key]
        del self.usage_order[lfu_key]
        print("DISCARD:", lfu_key)
