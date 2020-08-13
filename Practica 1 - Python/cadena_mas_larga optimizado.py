# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:58:28 2020

@author: santi
"""


from es_palindromo import a_letritas

def cadena_mas_larga(x):
    x = a_letritas(x)
    maslarga = ''
    ordenada = ''
    i = 0
    while len(x[i:]) > len(maslarga):
        for p in range(i+1,len(x)):
            if x[p] >= x[p-1]:
                ordenada = x[i:p+1]
                if len(ordenada) > len(maslarga):
                    maslarga = ordenada
            else:
                i = p
                break
    return maslarga

### TEST            
for entrada, salida in [['abcddd','abcddd'], ['abcazzzzzz','azzzzzz'], ['aa','aa'], 
                        ['abcabcdabcdabxyz','abxyz'], ['abcbcdefdefdefghz','defghz'],
                        ['zzxzz','xzz']]:
    if cadena_mas_larga(entrada) != salida:
        print('problema con ', entrada, 'está dando', cadena_mas_larga(entrada),
              'y debería dar', salida)
else:
    print('Todo piola')
