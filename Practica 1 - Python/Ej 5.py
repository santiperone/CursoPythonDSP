# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:03:51 2020

@author: santi
"""
## EJERCICIO 5

frase = 'Macri gato'
funcionando = True
x = input('Escribi "'+frase+'": ')
if x == frase:
    funcionando = False
else:
    while funcionando :
        x = input('Dale, Escribi "'+frase+'": ')
        if x == frase:
            funcionando = False
print('Muchas gracias.')
        