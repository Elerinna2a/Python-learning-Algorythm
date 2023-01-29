# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:18:10 2022

@author: Antony
"""

list1=list(range(1000))
n=len(list1)-1

def funcSum(list1):
    x=0
    for i in list1:
        x=i+x
    return x


def funcGauss(n):
    return n*(n+1)/2