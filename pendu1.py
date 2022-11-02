# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:33:11 2022

@author: Antony
"""
"""
faire une liste de choix aleatoire
faire afficher un mot dans la console avec en premiere lettre afficher
( mot aleatoire ? )
et le reste sous "_"
si une lettre est retrouver alors remplacer le "_" par la lettre correspondante
et quand on a trouver toute les lettre donc si il n'y a plus de "_" dire
qu'on a gagner

for l in solution:
    if l != solution[0:1]:
        affichage = affichage + "_ "
    else:
        affichage = affichage + solution [0:1]

"""

import random
choix = ["python", "htmlcss", "javascript", "github"]
mot_random= random.choice(choix)

mot_a_trouver=mot_random
affichage=""
lettre_trouve=""

for i in mot_a_trouver:
    if i != mot_a_trouver[0]:
        affichage = affichage + "_ "
    else:
        affichage = affichage + mot_a_trouver [0]
         
print("mot a deviner : ", affichage)
try1 = input("proposer une lettre : ")[0:1]









# def initialisationJeu(mot):
# ### Affiche uniquement des _ sauf pour la première lettre

        
# initialisationJeu(mot)
# # def verification(lettre,mot):
    
#     ### a coder
    
# def affichageMot(lettre,mot,mot_affiche_precedent):
# ### Afficher la lettre dans le mot, tout en gardant en mémoire le
# mot affiché précedemment.
# return mot_affiche

# def jeu(mot):
# gagne = False
# while not gagne:
# ###Jouer au jeu