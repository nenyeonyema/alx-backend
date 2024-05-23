#!/usr/bin/env python3
""" LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Caching """
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item
            self.cache_data[key] = item
            # Update the frequency
            self.frequency[key] += 1
            # Update the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                
                # If there are multiple least frequently used items, use LRU to discard
                if len(lfu_keys) > 1:
                    lru_key = next(k for k in self.usage_order if k in lfu_keys)
                    self.usage_order.remove(lru_key)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print(f"DISCARD: {lru_key}")
                else:
                    lfu_key = lfu_keys[0]
                    self.usage_order.remove(lfu_key)
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print(f"DISCARD: {lfu_key}")

            # Add the new item
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency
        self.frequency[key] += 1
        # Update the usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
