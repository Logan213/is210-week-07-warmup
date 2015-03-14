#!usr/bin/env python
# -*- coding: utf-8 -*-
"""A Function With a For Loop"""


def process_data(data):
    """Adds values in a list or tuple and finds average.

    Args:
        data(list or tuple): arg to be changed arithmetically using for loop

    Returns:
        tuple: sum of all list or tuple values, average of values

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)

    """
    mylist = data
    mysum = 0
    for item in mylist:
        item += mysum
        mysum = item
    myavg = float(mysum)/len(mylist)
    return (mysum, myavg)
