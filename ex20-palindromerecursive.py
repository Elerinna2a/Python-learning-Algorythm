# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:15:27 2022

@author: Antony
"""

def palindromRecursif(phrase):
    if len(phrase)<2:
        return True
    if phrase[0]!=phrase[-1]:
        return False
    else:
        return palindromRecursif(phrase[1:-1])
