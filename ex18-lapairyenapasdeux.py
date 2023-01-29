# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:14:04 2022

@author: Antony
"""

def paire(n):
    if n==0:
        return True
    return impaire(n-1)

def impaire(n):
    if n==0:
        return False
    return paire(n-1)


print(paire(10))
print(paire(7))
print(impaire(10))
print(impaire(7))
