# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:12:13 2022

@author: Antony
"""

def infiniteEcho():
    print("Echo")
    infiniteEcho()



def tripleEcho(n):
    
    if n==0:
        return
    print("Echo")
    tripleEcho(n-1)
    
tripleEcho(3)
