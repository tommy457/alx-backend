#!/usr/bin/env python3
"""
Module for index_range function.
"""
import csv
import math
from typing import List, Tuple, Dict


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ return a tuple of size two,
        containing a start index and an end index. """
        end_index = page_size * page
        start_index = end_index - page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieve a page of data from the dataset. """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        try:
            data = self.dataset()
            return data[start_index:end_index]

        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """" Return the pagination parameters """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        data_size = len(data)
        next_page = page + 1
        prev_page = page - 1
        return {
            "page_size": data_size,
            "page": page,
            "data": data,
            "next_page": next_page if next_page < total_pages else None,
            "prev_page": prev_page if prev_page > 0 else None,
            "total_pages": total_pages
        }
