# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:55:36 2020

@author: santi
"""


def es_periodica(x): 
    for i in range(len(x)//2,len(x)):
        if x[i-len(x[i:]):i] == x[i:]:
            return True
    return False

# for cadena in ('abcddd', 'abcdcdcd', 'aa', 'aaa', 'abab', 'abcabc', 'abcbcdefdefdef',):
#     if not es_periodica(cadena):
#         print('Hubo un problema con', cadena)
#         break
# else:
#     print('Todo piola')

# for cadena in ('', 'x', 'xy', 'xyx', 'uvwxyz', 'xyzx'):
#     if es_periodica(cadena):
#         print('Hubo un problema con', cadena)
#         break
# else:
#     print('Todo piola')
