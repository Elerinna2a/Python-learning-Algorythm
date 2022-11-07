# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:33:43 2022

@author: Antony
"""
import random
import string


# liste_3=[0, 1]

# for i in range(len(liste_3)-1):
#     b = liste_3[i-1]
#     c = liste_3[i-2]
#     d = b+c
#     liste_3.append(d)

def fibonacci(nb):
    if nb <= 0:
        return 0
    fibo_start=[0, 1]
    while len(fibo_start) <= nb:
        next_value=fibo_start[len(fibo_start) - 1] + fibo_start[len(fibo_start) - 2]
        fibo_start.append(next_value)
    return fibo_start
y=fibonacci(100)

def fibo_fibo():
    fibo = fibonacci(100)
    fibo2 = []
    for i in range(1,99):
        fibo2.append(fibo[i - 1] + fibo[i + 1])
    return fibo2
x=fibo_fibo()
        
    
    











# # code 2
# liste = []
# a=0

# while a in liste:
#     a+=1
#     if a == int(100-10):   
        
    