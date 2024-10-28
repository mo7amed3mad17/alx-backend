#!/usr/bin/env python3
""" Simple Helper Function"""

def index_range(page: int, page_size: int) -> tuple:
    start_index = (page) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
