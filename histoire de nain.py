# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:33:56 2022

@author: Antony
"""

# tableau_multi = [] 
# # tablea de a 0 a 9
# for i in range(10):
#     # creation de la colonne de 0 a 9
#     colonne=[]
#     # on multiplie tout
#     for j in range(10):
#         colonne.append(i*j)
#     # on ajoute la colonne dans un autre tableau
#     tableau_multi.append(colonne)

nain_1 = [1]
nain_2 = [2]
nain_3 = [4]
nain_4 = [8]
nain_5 = [16]
nain_6 = [32]
nain_7 = [64]

tableau = (nain_1, nain_2, nain_3, nain_4, nain_5, nain_6, nain_7)

def voleur(pesee):
    for i in range(len(tableau)):
        if pesee == sum(tableau):
            print("c'est ok")
        else:
            print("VOLEUR!")
voleur(127)

