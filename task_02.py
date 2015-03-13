#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""

import data

BALLETS = data.BALLETS


def myfunc(a_list):
    del a_list[11]
    a_list[1] = 'Swan Lake'
    a_list.append('Herman Schmerman')
    a_list.extend(('Don Quixote', 'Sylvia'))
    return [a_list]

myfunc(BALLETS)



