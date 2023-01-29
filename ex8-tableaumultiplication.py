# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:34:35 2022

@author: Antony
"""

table_multiplication=[]
for i in range(10):
    colonne=[]
    for j in range(10):
        colonne.append(i*j)
    table_multiplication.append(colonne)
print(table_multiplication[3][4])