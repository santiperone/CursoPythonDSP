# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:18:42 2020

@author: santi
"""


import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(-1,1,1000)
x = t**3
y = t**2

plt.figure(1)
plt.plot(x,y)
plt.grid()

x = np.sin(np.pi * t)
y = np.sin(2 * np.pi * t)

plt.figure(2)
plt.plot(x,y)
plt.grid()

x = (np.sin(np.pi * t)) ** 3
y = (1 - np.cos(np.pi * t)) * np.cos(np.pi * t)

plt.figure(3)
plt.plot(x,y)
plt.grid()

