# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:57:03 2020

@author: santi
"""
## FRASE CAPICUA

def limpia_frases(frase):
    frase = frase.lower()
    fraseout = ''
    for i in frase:
        if i in ' abcdefghijklmnñopqrstuvwxyz':
            fraseout += i
    return fraseout

frase = input('Escriba una frase: ')
frase = limpia_frases(frase)
listfrase = frase.split()
if listfrase == listfrase[::-1]:
    print('Felicidades, la frase es capicua.')
else:
    print('La frase no es capicua, una pena.')
    
        
    
    

