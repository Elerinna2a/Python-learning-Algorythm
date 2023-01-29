# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:00:02 2022

@author: Antony
"""

alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
clef = 7


def trouverIndiceLettre(lettre):
    cpt=0
    for i in alphabet:
        if i==lettre:
            return cpt
        cpt+=1
    print("error, this letter is not in the alphabet")
    
    
print(trouverIndiceLettre("e"))


def chiffrementCesar(phrase,clef):
    phraseChiffre = []
    for i in phrase:
        indiceActuel = trouverIndiceLettre(i)
        indiceNouveau_temp = indiceActuel+clef
        indiceNouveau = indiceNouveau_temp % len(alphabet)
        lettreNouveau = alphabet[indiceNouveau]
        phraseChiffre.append(lettreNouveau)
    return phraseChiffre


def dechiffrementCesar(phraseChiffre,clef):
    phraseClaire = []
    for i in phraseChiffre:
        indiceActuel = trouverIndiceLettre(i) #indice récupéré pour calcul
        indiceNouveau_temp = indiceActuel-clef #nouvel indice, hors tableau
        indiceNouveau = indiceNouveau_temp % len(alphabet) #modulo sur tableau tourant
        lettreNouveau = alphabet[indiceNouveau]
        phraseClaire.append(lettreNouveau)
    return phraseClaire


phraseChiffre = chiffrementCesar("le chiffrement de cesar",6)
print(phraseChiffre)
print(dechiffrementCesar(phraseChiffre,6))
