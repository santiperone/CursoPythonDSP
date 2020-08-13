# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:48:15 2020

@author: santi
"""

frase = input('Escriba una frase: '.lower())
frase = frase.translate({ord(c): None for c in '()%*!@#$'})
x1 = 0
x2 = 0
cont = 1
listfrase = []
funcionando = True
capicua = False

for letra in frase:
    if frase[x2] == ' ':
        listfrase.append(frase[x1:x2])
        x1 = x2+1
        x2 += 1
    else:
        x2 += 1
listfrase.append(frase[x1:x2])
        
while funcionando and cont <= (len(listfrase)/2):
    if listfrase[cont-1] == listfrase[-cont]:
        capicua = True
        cont += 1
    else:
        capicua = False
        funcionando = False
        
if capicua == True:
    print('Felicidades, la frase es capicua.')
else:
    print('La frase no es capicua, una pena.')


frase.translate()