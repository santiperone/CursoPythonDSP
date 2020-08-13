3# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:45:36 2020

@author: santi
"""

cantidad = 0
suma = 0
while cantidad < 10:
    numero = float(input('Ingrese un numero positivo: '))
    if numero > 0:
        cantidad += 1
        suma = suma + numero
    else:
        print('POSITIVO pelotudo')
print('La suma es',suma,)