#!/usr/bin/env python3
""" FIFOCache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Caching system """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
        len_item = len(self.cache_data)
        if key not in self.cache_data and len_item >= BaseCaching.MAX_ITEMS:
            first_in = self.order.pop(0)
            del self.cache_data[first_in]
            print(f"DISCARD: {first_in}")

        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
