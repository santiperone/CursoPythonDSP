# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:02:17 2020

@author: santi
"""


def collatz(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    return n

contmax = 0
nmax = 0
for i in range(1,1000000):
    cont = 0
    n = i
    while n > 1:    
        n = collatz(n)
        cont += 1
    if cont > contmax:
        contmax = cont
        nmax = i
    
        
print(nmax)
print(contmax)
    

     