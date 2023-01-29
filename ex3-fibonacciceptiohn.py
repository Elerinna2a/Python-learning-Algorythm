# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:23:43 2022

@author: Antony
"""

liste_fibo = [0,1]#j'initialise la liste de fibonacci

#Je construit la liste
for i in range(2,100):
        liste_fibo.append(liste_fibo[i-2]+liste_fibo[i-1])
liste_fibo_fibo=[]

#Je construit la fibo fibo
for i in range(1,99):
        liste_fibo_fibo.append(liste_fibo[i-1]+liste_fibo[i+1])
#Je duplique la liste
liste_fibo_fibo2 = liste_fibo_fibo[:]
#Je supprime les éléments qui se retrouvent dans les deux
for i in range(len(liste_fibo_fibo2)):
        if liste_fibo_fibo2[i] in liste_fibo:
            liste_fibo_fibo2.pop(i)
#J'additionne
somme=0
for i in liste_fibo_fibo2:
    somme+=i