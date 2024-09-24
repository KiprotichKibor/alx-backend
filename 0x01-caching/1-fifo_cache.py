#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

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
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key, None)
