# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:53:19 2022

@author: Antony
"""

import random

liste1=list("abcdefghijklmnopqrstuvwxyz")
liste2= []

for i in range(100):
    a=random.randint(0,25)
liste2.append(liste1[a])

def comptageSimple(lettre):
    a=0
    for i in liste2:
        if i==lettre:
            a=a+1
    return a

L = comptageSimple("a")

liste3= []

def comptageMultiple():
    for i in liste1:
        print(i)
        liste3.append(comptageSimple(i))
        
comptageMultiple()
