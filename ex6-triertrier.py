# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:31:42 2022

@author: Antony
"""

import random

liste1 = list(range(100))
liste_melangee = liste1[:]
random.shuffle(liste_melangee)


def maximum(liste):
    maxi=liste[0]
    id_maxi = 0
    for i in range(len(liste)):
        if liste[i]>maxi:
            maxi=liste[i]
            id_maxi=i
    return maxi,id_maxi

maxi_liste_melangee, id_maxi_liste_melangee =maximum(liste_melangee)

liste_triee=[]

for i in range(len(liste_melangee)):
    maximum_courant,id_maximum_courant=maximum(liste_melangee)
    liste_triee.append(maximum_courant)
    liste_melangee.pop(id_maximum_courant)