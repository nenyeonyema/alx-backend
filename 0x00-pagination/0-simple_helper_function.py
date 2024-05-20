#!/usr/bin/env python3
""" Pagination """


def index_range(page, page_size):
    """
     returns a tuple of size two containing
     a start index and an end index
    """

    offset = (page - 1) * page_size
    lastindex = offset + page_size
    return (offset, lastindex)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
