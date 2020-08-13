# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:35:01 2020

@author: santi
"""


def a_letritas(frase):
    frase = frase.lower()
    fraseout = ''
    for i in frase:
        if i in 'abcdefghijklmnñopqrstuvwxyz':
            fraseout += i
    return fraseout

def es_palindromo(x):
    x = a_letritas(x)
    return x == x[::-1]