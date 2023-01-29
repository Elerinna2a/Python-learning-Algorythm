# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:30:42 2022

@author: Antony
"""

def mutismum(phrase):
    
    
    phrase=list(phrase) #Je transforme ma phrase en liste
    for i in range(len(phrase)):#Je boucle sur mes indices
        if phrase[i]=="m":#Si j'ai un m
            phrase[i]="p"#Alors je le remplace par un p, si je bouclais sur les valeurs cela ne marcherait pas
        elif phrase[i]=="p":
            phrase[i]="m"
    return("".join(phrase))#Ici je transforme ma liste en une phrase à nouveau


print(mutismum(input("Vous vouliez dire ? ")))