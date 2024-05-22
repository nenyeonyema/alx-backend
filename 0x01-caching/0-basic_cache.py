#!/usr/bin/env python3
""" Base Caching """
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """Basic Cache """
    def put(self, key, item):
        """ Put initialize the dict """
        if key is None and item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Gets the key value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
