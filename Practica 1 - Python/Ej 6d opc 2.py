# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:47:41 2020

@author: santi
"""

### EJERCICIO 6D

b = 1
p = 2
funcionando = True
num = float(input('Ingrese un numero natural: '))
while num - int(num) != 0 or num <= 0:
    num = float(input('El numero debe ser natural: '))
while funcionando:
    if b**p == num:
        funcionando = False
        posible = True
    elif b**p < num and p < 5:
        p += 1
    elif b < num**0.5 + 1:
        b += 1
        p = 2
    else:
        funcionando = False
        posible = False
if posible == True:
    print('El numero es igual a '+str(b)+'^'+str(p))
else:
    print('La operacion no es posible')