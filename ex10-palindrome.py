# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:56:48 2022

@author: Antony
"""

def palindromeMot(mot):
    
    for i in range(int(len(mot)/2)):
        a=mot[-i-1]
        b=mot[i]
        print(f"{a} & {b}")
        if a!=b:
            return False
    return True


palindromeMot(input("mot? : "))


def transformationPhrase(phrase):
    phrase = phrase.lower()
    listePhrase=[]
    for i in phrase:
        if i == " ":
            a = 0
        if i == "," or i == "." or i == "?" or i == "!":
            a = 0
        if i == "é" or i =="è" or i =="ê":
            listePhrase.append("e")
        if i == "à":
            listePhrase.append("a")
        if i == "ù":
            listePhrase.append("u")
        if i in liste1:
            listePhrase.append(i)
    print(listePhrase)
    
    
def palindrome(phrase):
    if palindrome(transformationPhrase(phrase)):
        print("je suis un palindrome")
    else:
        print("je suis pas un palindrome")
palindrome("Élu par cette crapule !")