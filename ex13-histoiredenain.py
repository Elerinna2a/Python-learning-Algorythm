# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:02:22 2022

@author: Antony
"""

import random
##crÃ©ation des nain
nain=[0]*7
##nombres de lingot par nain
for i in range(7):
    nain[i]=random.randint(64, 100)
##crÃ©ation du nain escrot
liste_escroc = []
for i in range(7):
    liste_escroc.append(random.randint(0, 1))
##On modÃ©lise les sac des nains
sacNain=[0]*7

##On attribue les lingots des nains
for i in range(len(sacNain)):
    x=1
    if liste_escroc[i]==1:
        x=0.99
    sacNain[i]=[x]*nain[i]
##Faire la pesée sachant que on a le droit qu'à une seule pesée pour trouver le nain escrot.
balance = 0

for j in range(7):
    nbLingot = 2**j
    balance += sacNain[j][0]*nbLingot