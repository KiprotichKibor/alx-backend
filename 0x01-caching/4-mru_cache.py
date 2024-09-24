#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache defines a Most Recently Used (MRU) caching system
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
                if key not in self.cache_data:
                    mru_key, _ = self.cache_data.popitem(last=True)
                    print(f"DISCARD: {mru_key}")
                else:
                    self.cache_data.move_to_end(key)

            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item by key

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
