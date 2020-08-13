# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:11:50 2020

@author: santi
"""


## EJERCICIO 1:
num1 = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese otro numero entero: '))
if num1 == num2:
    print('Los numeros son iguales')
if num1 % num2 == 0:
    print('El primer numero es divisible por el segundo')
if num2 % num1 == 0:
    print('El segundo numero es divisible por el primero')
if num1 == num2**2:
    print('El primer numero es el cuadrado del segundo')
if num2 == num1**2:
    print('El segundo numero es el cuadrado del primero')
    