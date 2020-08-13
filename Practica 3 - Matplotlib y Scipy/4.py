# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:18:42 2020

@author: santi
"""


import numpy as np
from matplotlib import pyplot as plt

x = np.array([0,2,4,5])
m1 = np.array([1,0,4,4])
m2 = np.array([2,2,1,6])
mod = np.array([0,1,3,5])

plt.figure(1)
plt.plot(x, mod, 'b', label='Modelo')
plt.plot(x, m1, 'go', label='Medición 1')
plt.plot(x, m2, 'r--', label='Medición 2')
plt.plot(x, m2, 'r*')
plt.xlabel('Variable Dependiente')
plt.ylabel('Variable Independiente')
plt.grid()
plt.legend()