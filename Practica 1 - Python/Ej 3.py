# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:35:49 2020

@author: santi
"""

## Ejercicio 3

numero = float(input('Ingrese un numero: '))
if numero == int(numero):
    caracteres = len(str(numero))-1 
else:
    caracteres = len(str(numero))-1 
print('El numero tiene',caracteres,'caracteres')
