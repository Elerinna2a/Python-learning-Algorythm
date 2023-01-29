# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:14:52 2022

@author: Antony
"""

def maximum(list):
    if len(list) == 1:
        return list[0]
    else:
        m = maximum(list[1:])
        if m > list[0]:
            return m
        else:
            return list[0]