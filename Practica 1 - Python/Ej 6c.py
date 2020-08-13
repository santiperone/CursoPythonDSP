# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:32:53 2020

@author: santi
"""

## EJERCICIO 6a


x = 0
num = int(input('Ingrese un numero entero: '))
funcionando = True
if num == 0:
    raiz = 0
    funcionando = False
    cubo = True
else:
    while funcionando:
        if x**3 == abs(num):
            funcionando = False
            cubo = True
        elif x**3 > abs(num):
            funcionando = False
            cubo = False
        else:
            x += 1
    raiz = x
if cubo == False:
    print('El numero no es un cubo perfecto')
elif num >= 0:
    print('La raiz cubica de',num,'es',raiz)
else:
    print('La raiz cubica de',num,'es -'+str(raiz))  
