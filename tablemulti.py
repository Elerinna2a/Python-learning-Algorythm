# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 08:13:39 2022

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

multiX=multi(11)