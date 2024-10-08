#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with hypermedia pagination information.

        Args:
        index (int): The start index of the current page (default: None)
        page_size (int): The size of the page (default: 10)

        Returns:
        Dict: A dictionary containing pagination information and data
        """
        assert index is None \
            or (isinstance(index, int) and index >= 0), \
            "Index must be a non-negative integer"

        indexed_dataset = self.indexed_dataset()
        data_length = len(indexed_dataset)

        if index is None:
            index = 0

        assert index < data_length, "Index out of range"

        data = []
        current_index = index
        next_index = index + page_size

        while len(data) < page_size and current_index < data_length:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        while current_index < data_length and len(data) < page_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
