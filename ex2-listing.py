# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:20:43 2022

@author: Antony
"""

import random

def nomDeDomaine():
    liste_domaine=["gmail", "yahoo", "wanadoo", "hotmail", "caramail"]
    liste_pays = [".fr", ".com", ".ru", ".net", ".li", ".eu"]
    a=random.randint(0,len(liste_domaine)-1)#ici j'utilise les indices
    b=random.choice(liste_pays)#ici je random sur les valeurs
    return liste_domaine[a]+b

import string

def motAleatoire(taille):
    mot=""
    liste_voyelle = ["a","e","u","i","o","y"]
    liste_consonne = string.ascii_lowercase # j'initialise ma liste de consonne
    for i in liste_consonne:#j'enleve les voyelles des consonnes
        if i is in liste_voyelle:
            liste_consonne.remove(i)
    voyant = False #Je met en place un interrupteur pour alterner entre voyelle et consonne.
    for i in range(taille):
        a = random.choice(liste_voyelle)
        b = random.choice(liste_consonne)
        if voyant:
            mot+=a
        else:
            mot+=b
        voyant = not voyant
return mot

liste_mail = []
for i in range(100):
    taille = random.randint(2,12)
    liste_mail.append(motAleatoire(taille)+nomDeDomaine())
