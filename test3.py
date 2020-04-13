# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:42:20 2020

@author: songl
"""

from numpy.random import rand
values = rand(10000,6)
lst = [list(row) for row in values]
tup = tuple(tuple(row) for row in values)















