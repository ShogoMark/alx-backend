#!/usr/bin/env python3
"""function that returns a tuple of index of page"""


def index_range(page: int, page_size: int) -> tuple:
    """function takes in args page & page size"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    new_tuple = (start_index, end_index)

    return new_tuple
