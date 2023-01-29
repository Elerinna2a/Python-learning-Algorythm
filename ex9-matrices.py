# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:35:13 2022

@author: Antony
"""

A = [list(range(2)),list(range(3,5))]
B = [list(range(3,5)),list(range(2))]



def addition(A,B):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        print("Ces matrices ne sont pas aditionnables")
        return False
    C = len(A)*[len(A[0])*[0]]
    for line in range(len(A)):
        for row in range(len(A[0])):
            C[line][row]=A[line][row]+B[line][row]
            return C
C = addition(A,B)


def multiplication(A,B):
    if len(A)!=len(B[0]) or len(A[0])!=len(B):
        print("Ces matrices ne sont pas multipliables")
        return False
    C = len(A)*[len(B[0])*[0]]
    for line in range(len(A)):
        for row in range(len(A[0])):
            for elt in range(len(A)):
                C[line][row]+=A[line][elt]+B[elt][row]
    return C
D = multiplication(A, B)
