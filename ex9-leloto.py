# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:55:39 2022

@author: Antony
"""

import random
liste1=list(range(1,50))
liste2= []

def tirage(liste):
    a=liste1[random.randint(1,len(liste))]
    liste1.remove(a)
    liste2.append(a)
    return liste2
# print(tirage(liste1))

def loto(liste):
    for i in range(5):
        tirage(liste)
    return liste2
print(loto(liste1))