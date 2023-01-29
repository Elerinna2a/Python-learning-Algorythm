# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:06:25 2022

@author: Antony
"""

liste_naturelle = list(range(100))

def funAffichage(liste):
    for i in liste:
        print(i)
        
funAffichage(liste_naturelle)

def funParcoursChelou(liste):
        boole=True
        while i<len(liste)-1:
            if boole:
                i=i+3
                print(f"{liste[i]} & est impair")
                boole= not boole
            else:
                i=i-1
                print(f"{liste[i]} & est pair")
                boole= not boole
            
funParcoursChelou(liste_naturelle)

def funTrierPaire(liste):
    liste_paire= []
    liste_impaire= []
    for i in liste:
        if i %2==0:
            liste_paire.append(i)
        else:
            liste_impaire.append(i)
            return liste_paire, liste_impaire
liste_paire1, liste_impaire1 = funTrierPaire(liste_naturelle)
