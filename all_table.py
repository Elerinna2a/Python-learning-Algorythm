# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:10:01 2022

@author: abell
"""
# liste0=list(range(0,10,0))
# liste1=list(range(1,10,1))
# liste2=list(range(2,20,2))
# liste3=list(range(3,30,3))
# liste4=list(range(4,40,4))
# liste5=list(range(5,50,5))
# liste6=list(range(6,60,6))
# liste7=list(range(7,70,7))
# liste8=list(range(8,80,8))
# liste9=list(range(9,90,9))
# liste10=list(range(10,100,10))

# listeAll=[liste0,liste1,liste2,liste3,liste4,liste5,liste6,liste7,liste8,liste9,liste10]


def multi(x):
    res = []
    for i in range(x):
        line = []
        for j in range(x):
            line.append(i*j)
        res.append(line)
    return res

multiX=multi(10)
