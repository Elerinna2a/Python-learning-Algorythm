# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:33:13 2022

@author: Antony
"""

x = list(range(0,100))
y = []

for i in x:
    y.append(-((i)**2)-2*i+1000)
    
z=[x,y]
## Ainsi
z[0][0]
## Me permet d'accéder à la première valeur du premier tableau