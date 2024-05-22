#!/usr/bin env python3
""" Most Recent Update MRU """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching """
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item's order
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the key to the usage order and update the cache
        self.usage_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update the usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
