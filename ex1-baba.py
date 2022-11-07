# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:13:32 2022

@author: Antony
"""
import random
liste=list(range(101))
liste2=liste[:]
liste2.pop(liste2[50])

liste3 = []
for i in liste:
    a=random.randint()
    liste3.append(a)
    liste.pop(a)