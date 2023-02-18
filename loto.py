# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:42:50 2022

@author: abell
"""

import random
liste1=list(range(1,50))
liste2= []

def tirage(liste1):
    a=liste1[random.randint(1,len(liste1))]
    liste1.remove(a)
    liste2.append(a)
    return liste2
# print(tirage(liste1))

def loto(liste1):
    for i in range(5):
        tirage(liste1)
    return liste2
print(loto(liste1))