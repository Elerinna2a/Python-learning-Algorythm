# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:04:40 2022

@author: Antony
"""

def maximum(T):
    if len(T) == 1:
        return T[0]
    
    # principe de la recherche dichotomique
    m = len(T)//2
    max1 = maximum(T[:m])
    max2 = maximum(T[m:])
    if max1 > max2:
        return max1
    return max2