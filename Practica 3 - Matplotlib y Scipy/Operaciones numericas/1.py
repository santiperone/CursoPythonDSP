# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:20:51 2020

@author: santi
"""
import numpy as np
import matplotlib.pyplot as plt

datos_x = np.linspace(0,2,10)
datos_y = datos_x

def area_rectangulos(datos_x, datos_y):
    area = 0
    delta_x = (datos_x[-1]-datos_x[0]) / (len(datos_x)-1)
    for i in range(0, len(datos_x)):
        area += delta_x * datos_y[i]
        print(area)
    return area

def area_trapecios(datos_x, datos_y):
    area = 0
    h = (datos_x[-1]-datos_x[0]) / (len(datos_x)-1)
    for i in range(0, len(datos_y)-1):
        area += (datos_y[i]+datos_y[i+1]) * h / 2
        print(area)
    return area

def cumtrapz(datos_x, datos_y):
    area = 0
    h = (datos_x[-1]-datos_x[0]) / (len(datos_x)-1)
    out = np.array([0])
    for i in range(0, len(datos_y)-1):
        # print((datos_y[i]),(datos_y[i+1]))
        area += (datos_y[i]+datos_y[i+1]) * h / 2
        out = np.hstack([out, area])
    return out

delta_x = (datos_x[-1]-datos_x[0]) / (len(datos_x)-1)
vector_area = np.cumsum(datos_y) * delta_x
plt.figure(6)
plt.plot(datos_x, datos_y, label='Función original')
plt.plot(datos_x, vector_area, 'r', label='Función área')
plt.plot(datos_x, cumtrapz(datos_x, datos_y), 'g', label='Función área trapz')
plt.xlabel('Variable independiente')
plt.ylabel('Variable dependiente')
plt.title('Área con cumsum')
plt.legend()
plt.grid()