# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 08:30:14 2022

@author: Antony
"""

alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def indice_lettre(lettre):
    cpt=0
    for i in alphabet:
        if i==lettre:
            return cpt
        cpt+=1
    print("Ao coco, cette lettre n'est pas dans ton alphabet")
        
# print(indice_lettre("z"))

def code_vigenere(phrase, clef):
    phrase_code = []
    clef_code = []
    y = 0
    for n in clef:
        clef_code.append(indice_lettre(n))
    for i in phrase:
        chiffrement_phrase_new = indice_lettre(i)
        phrase_clef_new = chiffrement_phrase_new+clef_code[y % len(clef_code)]
        idx_new = phrase_clef_new % len(alphabet) 
        new_lettre = alphabet[idx_new]
        phrase_code.append(new_lettre)
    return (phrase_code)

print(code_vigenere("jadoreecouterlaradio","musique"))


def decode_vigenere(phrase, clef):
    phrase_decodee = []
    clef_decode = []
    x = 0 
    for n in clef: 
        clef_decode.append(indice_lettre(n)) 
    for i in phrase:
        chiffrement_phrase = indice_lettre(i) 
        phrase_clef = chiffrement_phrase-clef_decode[x % len(clef_decode)]
        idx = phrase_clef % len(alphabet)
        nouvelle_lettre = alphabet[idx]
        phrase_decodee.append(nouvelle_lettre)
    return (phrase_decodee) 

# print(decode_vigenere("wnqadrrpagfrdyndnqva", "musique")) 



    
