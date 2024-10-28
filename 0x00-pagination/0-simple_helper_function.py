#!/usr/bin/env python3
""" Simple Helper Function"""


def index_range(page: int, page_size: int) -> tuple:
    """ A function that return the statrt and end indeces of the data """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
