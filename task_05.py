#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function to reverse a list"""


def flip_keys(to_flip):
    """a list with nested args.

    Args:
        to_flip(list): a list with nested arguments.

    Returns:
        List with each item reversed by for loop and slicing.

    Examples:

        >>> flip_keys([(1, 2, 3), 'abc'])
        [(3, 2, 1), 'cba']

    """
    myindex = 0
    for item in to_flip:
        to_flip[myindex] = item[::-1]
        myindex += 1
    return to_flip
