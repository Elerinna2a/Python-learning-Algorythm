# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:06:53 2022

@author: abell
"""
import random
liste1=[]
for i in range(100): # parcourir toute la liste
    a=random.randint(0,100)
    liste1.append(a)

# trouver le maxi
def maxi(liste1):
    x = liste1[0]
    for i in liste1:
        if x<i:
            x=i
    print(x)
maxi(liste1)

# trouver le mini
def maxi(liste1):
    y = liste1[0]
    j=0
    for i in liste1:
        if y>i:
            y=i
            pos_mini=j
        j+=1
    print(y,pos_mini)
maxi(liste1)
        
    

    
    
    
    
    


            
    
    
