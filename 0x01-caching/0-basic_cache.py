#!/usr/bin/env python3
""" Basic_Caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system without a limit
    """

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        return self.cache_data.get(key, None)
