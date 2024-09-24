#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used (LFU) caching system
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_frequency = defaultdict(int)
        self.frequency_list = defaultdict(OrderedDict)
        self.min_frequency = 0

    def put(self, key, item):
        """
        Add an item in the cache

        Args:
            key: The key to add
            item: The value to associate with the key

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._remove_least_frequent()

        self.cache_data[key] = item
        self.keys_frequency[key] = 1
        self.frequency_list[1][key] = None
        self.min_frequency = 1

    def get(self, key):
        """
        Retrieve an item by key

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        if key in self.cache_data:
            self._update_frequency(key)
            return self.cache_data[key]
        return None

    def _update_frequency(self, key):
        """
        Update the frequency of a key
        """
        freq = self.keys_frequency[key]
        self.keys_frequency[key] += 1
        del self.frequency_list[freq][key]
        if not self.frequency_list[freq]:
            if freq == self.min_frequency:
                self.min_frequency += 1
            del self.frequency_list[freq]
        self.frequency_list[freq + 1][key] = None

    def _remove_least_frequent(self):
        """
        Remove the least frequently used item
        """
        lfu_key, _ = \
            self.frequency_list[self.min_frequency].popitem(last=False)
        del self.cache_data[lfu_key]
        del self.keys_frequency[lfu_key]
        print(f"DISCARD: {lfu_key}")
