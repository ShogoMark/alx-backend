#!/usr/bin/env python3
"""function that returns a tuple of index of page"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """function takes in args page & page size"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    new_tuple = (start_index, end_index)

    return new_tuple


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
        """function takes in page & page_size, returns a list"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        return dataset[start_index:end_index]


    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        next_page = page + 1
        prev_page = page - 1

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        total_pages = len(dataset) // page_size

        if next_page > end_index or prev_page == 0:
            return None

        return "page_size: {}, page: {}, data: {}, next_page: {}, "\
        "prev_page: {}, total_pages: {}".format(page_size, page,
                                           str(get_page(
                                                self,
                                                page=1,
                                                page_size=10)),
                                           next_page,
                                           prev_page,
                                           total_pages)
