# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:05:57 2022

@author: Antony
"""


def tableau_vigenere () :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    tableau = []
    #pour chaque lettre de l'alphabet
    for i in range (0,26) :
        tableau.append(alphabet) #on ajoute l'alphabet dans le tableau vide
        alphabet = alphabet [1:26] + alphabet [0] #on prend le premier caratere et on le deplace a la fin
    return tableau # on renvois le tableau dans une variable pour l'afficher dans le variable explorer
 
def methode_vigenere (message, cle, tableau):
    alphabet = tableau [0] # contient l’alphabet (premiere ligne du tableau)
    resultat = "" # contiendra le message code
    # on parcourt le message
    for i in range (0, len (message)) :    
        # j est la position de la lettre dans le cle
        # associee a la lettre i dans le message
        # % retourne le reste d’une division entiere
        j = i % len (cle)
        a = alphabet.find (message [i]) # numero de la lettre message [i]
        b = alphabet.find (cle [j]) # numero de la lettre cle [j]
        c = tableau [b][a]
        resultat += c
    return resultat
 
 
message = input("message a crypter ? : ")
cle = input("la clé ? : ")
tableau2 = tableau_vigenere ()
code = methode_vigenere(message, cle, tableau2)
print ("clé : ")
print (cle)
print ("message : ")
print (message)
print ("message codé : ")
print (code)
