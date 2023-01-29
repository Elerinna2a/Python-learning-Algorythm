# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:16:03 2022

@author: Antony
"""

def arbreNoel(n):
    
    for i in range(1,n+1,2):
        print(int((n-i)/2)*" "+i*"*")
        
arbreNoel(10)