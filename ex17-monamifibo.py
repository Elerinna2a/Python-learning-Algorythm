# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:13:08 2022

@author: Antony
"""
def fiboCursif(n):
    if n in [0,1]:
        return n
    return fiboCursif(n-1)+fiboCursif(n-2)

liste_fibo=[]

for i in range(10):
    liste_fibo.append(fiboCursif(i))
