# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:52:50 2022

@author: abell
"""

list1=list(range(100))

def funcP(list1):
    for i in list1:
        print(f"je suis l'élement {i}")

def funcP2(list1):
    i=0
    boole=True
    while i<len(list1)-1:
        if boole:
            i=i+3
            print(f"{list1[i]} & est impair")
            boole= not boole
        else:
            i=i-1
            print(f"{list1[i]} & est pair")
            boole= not boole
funcP2(list1)


def funcP3(list1):
    liste_paire= []
    liste_impaire= []
    for i in list1:
        if i %2==0:
            liste_paire.append(i)
        else:
            liste_impaire.append(i)
            return liste_paire, liste_impaire
liste_paire1, liste_impaire1=funcP3(list1)
    
        
    



