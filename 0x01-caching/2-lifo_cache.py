#!/usr/bin/env python3
"""LIFO """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # LIFO: remove the last item added (most recently added item)
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # If the key is already in the cache, we need to remove it from the stack
        if key in self.cache_data:
            self.stack.remove(key)
        
        # Add the key to the stack and update the cache
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
