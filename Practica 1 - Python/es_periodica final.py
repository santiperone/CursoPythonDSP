# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:44:57 2020

@author: santi
"""


def es_periodica(x):
    # if x[:len(x)//2] == x[len(x)//2:]:
    #     return True
    
    for i in range(len(x)//2,len(x)):
        print(i)
        print(len(x[i:]))
        print(x[i-len(x[i:])
        print(x[i:])
        print('')
        if x[i-len(x[i:]):i] == x[i:]:
            return True
    return False

es_periodica('cabbbbbbbbbaca')