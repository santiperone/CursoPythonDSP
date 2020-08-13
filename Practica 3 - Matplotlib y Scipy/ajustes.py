# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:38:26 2020

@author: santi
"""

from numpy.linalg import inv

def cuad_min(datosX, datosY, n):
"""datos_x y datos_y son arrays.
n es el grado del polinomio de ajuste
"""
cols = n + 1
fils = len(datos_x)
A = np.zeros([fils, cols])
for i in range(0, fils):
for j in range(0, cols):
A[i, j] = (datos_x[i])**j
coefs = inv((A.T) @ A) @ (A.T) @ datosY
coefs = coefs[::-1]
return coefs


def ajuste_potencial(x, y):
(c1, c2) = cuad_min(np.log(x), np.log(y) ,1)
alfa = c1
beta = np.exp(c2)
return (beta, alfa)