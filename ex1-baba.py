# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:17:35 2022

@author: Antony
"""
import random

liste1 = list(range(101))
liste2 = liste1[:]


def middle():
    liste2.pop(int(len(liste2)/2))
    
middle()

## Une façon de faire
def melanger():
    liste_melange=[]
    for i in range(len(liste2)):
        a=random.randint(0,len(liste2)-1)
        liste_melange.append(liste2[a])
        liste2.pop(a)
    return liste_melange
liste1=melanger()


## Une autre façon de le faire
def shuffle():
    for i in range(500):
        a=random.randint(0,len(liste1)-1)
        liste1.append(liste1[a])
        liste1.pop(a)
shuffle()


def whereIsBrian(listeComplete,listeIncomplete):
    for i in range(len(listeComplete)):
        isIn = False
        for j in listeIncomplete:
            if j==listeComplete[i]:
                isIn = True
        if not isIn:
            return i
chiffre = whereIsBrian(liste1,liste2)
