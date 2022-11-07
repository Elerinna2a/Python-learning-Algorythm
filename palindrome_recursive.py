# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:07:53 2022

@author: Antony
"""

def palindrome(ch):
    if len(ch) == 1:
        return print("c'est un palindrome")
    if ch[0] == ch[-1]:
        return palindrome(ch[1:len(ch)-1])
    return print("ce n'est pas un palindrome")

mot = input(" palindrome ? : ")
print(palindrome(mot))