#!/usr/bin/env python3

""" a function named index_range that takes two integer
 arguments page and page_size.
 he function should return a tuple of size two containing
  a start index and an end index corresponding to the range
   of indexes to return in a list for
 those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import List, Tuple
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ a function to get the start and end of an idex """

    return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ a function that gets page based on page number """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexs = index_range(page, page_size)
        try:
            return self.dataset()[indexs[0]:indexs[1]]
        except IndexError:
            return []
