# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 07:53:39 2022

@author: Antony
"""

liste1=list(range(100))


def fonction_affichage(liste):
    for i in liste:
        print(i)
fonction_affichage(liste1)

def fonction_alternate(liste):
    a=True
    i=0
    while i<len(liste)-1:
        if a:
            i=i+3
            print(f"{liste[i]} est impair")
            a= not a
        else:
            i=i-1
            print(f"{liste[i]} est pair")
            a= not a
fonction_alternate(liste1)

def fonction_tri(liste):
    liste_paire= []
    liste_impaire = []
    for i in liste:
        if i %2==0:
            liste_paire.append(i)
        else:
            liste_impaire.append(i)
            return liste_paire, liste_impaire
liste_paire1, liste_impaire1 = fonction_tri(liste1)