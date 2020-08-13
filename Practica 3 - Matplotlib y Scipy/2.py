# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:13:50 2020

@author: santi
"""

import numpy as np
from matplotlib import pyplot as plt

datos_x = np.linspace(0,1,1000)
datos_y = 3 * datos_x**2 + 5
plt.figure(1)
plt.plot(datos_x,datos_y)
plt.grid()

datos_y = 2 ** datos_x - 1
plt.figure(2)
plt.plot(datos_x,datos_y)
plt.grid()

datos_y = np.sin(4 * np.pi * datos_x)
plt.figure(3)
plt.plot(datos_x,datos_y)
plt.grid()

datos_y = datos_x** 5 - datos_x**4 + datos_x**3 - datos_x**2 - 2*datos_x + 2
plt.figure(4)
plt.plot(datos_x,datos_y)
plt.grid()