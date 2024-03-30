#!/usr/bin/env python3
"""
Module for index_range function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index."""
    end_index = page_size * page
    start_index = end_index - page_size

    return (start_index, end_index)
