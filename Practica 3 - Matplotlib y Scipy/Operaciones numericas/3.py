# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:55:40 2020

@author: santi
"""
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [9.53647, 151.323, 2223.38, 16441.1, 78212.4,
280053, 823687, 2.09733e+06, 4.78319e+06,
1.00003e+07]

menor_error = 1000
for i in range(1,50):
    coef = np.polyfit(x,y,i)
    print(np.mean((np.polyval(coef,x)-y)**2))
    if np.mean((np.polyval(coef,x)-y)**2) < menor_error:
        menor_error = np.mean((np.polyval(coef,x)-y)**2)
        polinomio = np.polyval(coef,x)
        print(coef)

x2 = np.linspace(1, 10,1000)
p2 = np.polyval(coef, x2)
        
plt.figure(1)
plt.plot(x, y, 'bo',label='Función original')
# plt.plot(x, polinomio, 'r', label='Mejor aproximacion')
plt.plot(x2, p2, 'g', label='a')
plt.xlabel('Variable independiente')
plt.ylabel('Variable dependiente')
# plt.title('Área con cumsum')
plt.legend()
plt.grid()