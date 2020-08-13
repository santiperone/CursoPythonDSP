# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:55:27 2020

@author: santi
"""
from es_palindromo import a_letritas

def cadena_mas_larga(x):
    x = a_letritas(x)
    maslarga = ''
    ordenada = ''
    inicio = 0
    for i in range(inicio,len(x)):
        for p in range(i+1,len(x)):
            if x[p] >= x[p-1]:
                ordenada = x[i:p+1]
                if len(ordenada) > len(maslarga):
                    maslarga = ordenada
            else:
                inicio = p
                break
    return maslarga

### TEST            
for cadena in ('abcddd', 'abcazzzzzz', 'aa', 'abcabcdabcdeabxyz', 'abcbcdefdefdefh'):
    if not cadena_mas_larga(cadena):
        print('Hubo un problema con', cadena)
        break
else:
    print('Todo piola')