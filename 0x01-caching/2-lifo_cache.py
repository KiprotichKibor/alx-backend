#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a LIFO caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache

        Args:
            key: The key to add
            item: The value to associate with the key

        Returns:
            None
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.order.pop()
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item by key

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key, None)
