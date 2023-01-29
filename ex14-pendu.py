# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:03:54 2022

@author: Antony
"""

def initialisationJeu(mot):
    mot_initial = list(mot)
    for i in range(1,len(mot)):
        mot_initial[i]="_"
    return mot_initial


def verification(lettre,mot):
    if lettre in mot:
        return True
    else:
        return False


def affichageMot(lettre, mot, mot_affiche_precedent):
    if mot_affiche_precedent is not list:
        mot_affiche_precedent =list(mot_affiche_precedent)
    for i in range(len(mot)):
        if mot[i]==lettre:
            mot_affiche_precedent[i]=mot[i]
    return mot_affiche_precedent



def jeu(mot):
    gagne = False
    vie=5
    mot_affiche_precedent=initialisationJeu(mot)
    print("".join(mot_affiche_precedent))
    while not gagne:
        lettre_demande = input("Quelle lettre ?")
        if len(lettre_demande)!=1:
            print("Recommencez la saisie")
            continue
        else:
            if verification(lettre_demande,mot):
                print("Bien joué")
                
mot_affiche_precedent=affichageMot(lettre_demande,mot,mot_affiche_precedent)
                print("".join(mot_affiche_precedent))
            else:
                vie-=1
                if vie<0:
                    print("C'est perdu !")
                    return
                print(f"Dommage il ne te reste que {vie} coups")
            gagne=mot_affiche_precedent==list(mot)
        print("Bravo !")
        
        
jeu("test")
