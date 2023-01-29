# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:24:48 2022

@author: Antony
"""

import random

def journee():
    a=random.randint(1,3)
    b=random.randint(1,3)
    c=random.randint(1,3)
    return list([a,b,c])


def semaine():
    liste_semaine=[]
    for i in range(7):
        liste_semaine.append(journee())
    return liste_semaine


def mois():
    liste_mois = []
    for i in range(4):
        liste_mois.append(semaine())
    return liste_mois


def annee():
    liste_annee = []
    for i in range(12):
        liste_annee.append(mois())
    return liste_annee

annee_aleatoire = annee()


def simulation(annee):
    travail = 10
    repos = 10
    joie = 10
    for m in annee:
        for s in m:
            for i in s:
                for j in i:
                    if j==1:
                        if repos<0:
                            print("fatigué")
                        elif joie<0:
                            print("triste")
                        else:
                            travail+=2
                        repos-=2
                        joie-=1
                    if j==2:
                        if travail <0:
                            print("chomeur")
                        elif repos<0:
                            print("fatigué")
                        else:
                            joie+=2
                        repos-=1
                        travail-=1
                    if j==3:
                        repos+=3
                        travail-=1
    return(travail,repos,joie)

test = simulation(annee_aleatoire)

def minimumIndice(liste):
    mini=liste[0]
    id_mini=0
    for i in range(len(liste)):
        if liste[i]<mini:
            mini=liste[i]
            id_mini=i
        return id_mini
    
    
def simulationOptimisee():
    travail = 10
    repos = 10
    joie = 10
    annee=[]
    ##Premier jour aléatoire, pas obligatoire
    annee.append(journee())
    for a in range(365):
        journee_suivante=[]
        for j in annee[a]:
            if j==1:
                repos+=3
                travail-=1
            if j==2:
                if travail <0:
                    print("chomeur")
                elif repos<0:
                    print("fatigué")
                else:
                    joie+=2
                repos-=1
                travail-=1
            if j==3:
                if repos<0:
                    print("fatigué")
                elif joie<0:
                    print("triste")
                else:
                    travail+=2
                repos-=2
                joie-=1
            score = [repos,joie,travail]
            activite_suivante = minimumIndice(score)+1
            journee_suivante.append(activite_suivante)
        print(journee_suivante)
        print(score)
        annee.append(journee_suivante)
    return score

test2=simulationOptimisee()









