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
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """function to take index&page size as argument to return dict"""
        dataset_length = len(self.dataset())

    # If index is not provided or is out of range, set it to 0
        if index is None or not 0 <= index < dataset_length:
            index = 0

    # Calculate the next index to query with
        next_index = min(index + page_size, dataset_length)

    # Get the current page of data from the dataset
        current_page_data = [self.indexed_dataset().get(i)
                             for i in range(index, next_index)]

    # Check if any items were deleted between index and next_index
        deleted_items = [i for i in range(index, next_index)
                         if self.indexed_dataset().get(i) is None]

    # If there were deleted items, adjust the next_index
        if deleted_items:
            next_index += len(deleted_items)
            current_page_data = [self.indexed_dataset().get(i)
                                 for i in range(index, next_index)]

    # Create the result dictionary
        result = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": current_page_data
        }

        return result
