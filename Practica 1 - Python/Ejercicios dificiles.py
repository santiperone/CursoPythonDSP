# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:00:37 2020

@author: santi
"""

### DE VERDAD 1
def unidades(n):
    """
    Recibe un numero entero y devuelve su cifra en la posicion de las unidades.

    """
    a = int(n)
    b = str(a)
    c = b[-1]
    return int(c)

def al_menos_dos_impares(a,b,c):
    lista = [a,b,c]
    cont = 0
    for i in lista:
        if cont >= 2:
            return True
        elif i % 2 != 0:
            cont += 1
    return False

def es_primo(n):
    """
    Recibe un numero n y dice si es primo.

    """
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

def lista_divisores(n):
    """
    Recibe un numero n y devuelve una lista de sus divisores

    """ 
    lista = []
    for i in range(1,n):
        if n % i == 0:
            lista.append(i)
    return lista

def suma_divisores(n):
    """
    Recibe un numero n y devuelve la suma de sus divisores

    """ 
    suma = 0
    for i in lista_divisores(n):
        suma += i
    return suma

def son_amigos(a,b):
    return a == suma_divisores(b) and b == suma_divisores(a)

suma = 0
a = 1
while a < 10000:
    if son_amigos(a,suma_divisores(a)) and a != suma_divisores(a):
        print(a)
        print(suma_divisores(a))
        print()
        suma += a + suma_divisores(a)
        a = suma_divisores(a)+1
    else:
        a +=1
        