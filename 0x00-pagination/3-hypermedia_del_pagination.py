#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ a function that returns dict with hypered index """
        dataset = self.indexed_dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        assert index is not None and 0 <= index < total_pages
        data = []
        current_index = index
        while len(data) < page_size and current_index < total_items:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1
        next_index = current_index if current_index < total_items else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
