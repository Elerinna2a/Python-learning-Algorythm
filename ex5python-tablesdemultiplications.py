# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:19:29 2022

@author: Antony
"""

def multi(x):
    res = []
    for i in range(x):
        line = []
        for j in range(x):
            line.append(i*j)
        res.append(line)
    return res
multiX=multi(10)