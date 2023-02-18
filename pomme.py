# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:01:23 2022

@author: abell
"""

list1=list(range(1000))
n=len(list1)-1

"""def funcSum(list1):
    somme=sum(list1)
    print(somme)
"""

# fonction sum est ce qu'il y a plus bas
def funcSum(list1):
    x=0
    for i in list1:
        x=i+x
    return x



def funcGauss(n):
    return n*(n+1)/2

print(funcSum(list1))
print(funcGauss(n))