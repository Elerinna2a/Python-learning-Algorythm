# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:50:37 2022

@author: Antony
"""

def pair(n):
    if n == 1:
        return False
    return impair(n-1)
 
 
def impair(n):
    if n == 1:
        return True
    return pair(n-1)
    