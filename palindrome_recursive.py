# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:07:53 2022

@author: Antony
"""

def palindrome(mot):
    if len(mot) == 1:
        return print("c'est un palindrome")
    if mot[0] == mot[-1]:
        return palindrome(mot[1:len(mot)-1])
    return print("ce n'est pas un palindrome")

mot = input(" palindrome ? : ")
print(palindrome(mot))