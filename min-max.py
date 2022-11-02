# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 08:16:55 2022

@author: Antony
"""

import random
liste = []
for i in range(100):
    a=random.randint(0,100)
    liste.append(a)
    
def max_liste(liste):
    x = liste[0]
    for i in liste:
        if i < x:
            x=i
        print(x)
max_liste(liste)
        
def mini(liste):
    y = liste [0]
    j=0
    for i in liste:
        if y > i:
            y=i
            pos_mini=j
        j+=1
    print(y,pos_mini)
    
mini(liste)