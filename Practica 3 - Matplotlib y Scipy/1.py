# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:24:32 2020

@author: santi
"""

import numpy as np
from matplotlib import pyplot as plt

datos_x = np.array([0,1,2,3,4,5,6])
datos_y = np.array([0,2,4,4,5,6,7])

plt.figure(1)
plt.plot(datos_x,datos_y)
plt.grid()

datos_x = np.array([0.0,0.5,1.0,1.0,1.5,2.0,2.0,2.5,3.0])
datos_y = np.array([0,0,0,1,1,1,0,0,0])
plt.figure(2)
plt.plot(datos_x,datos_y)
plt.grid()

datos_x = np.array([-1,0,1,0,-1])
datos_y = np.array([0,1,0,-2,0])
plt.figure(3)
plt.plot(datos_x,datos_y)
plt.grid()