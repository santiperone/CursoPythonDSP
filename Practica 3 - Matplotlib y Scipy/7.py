# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:28:11 2020

@author: santi
"""

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

ang = np.empty(0)
mag = np.empty([0,806])
for file in list(Path('./Directividad').glob('*.txt')):
    t = np.loadtxt(str(file), skiprows = 2, usecols = [0,1])
    print(t)
    ang = np.hstack([ang,(int((str(file)[25:-5])))])
    mag = np.vstack([mag,t[:,1]])
freq = t[:,0]
    
ang = np.hstack([-ang[1:][::-1],ang])
X, Y = np.meshgrid(freq,ang)
mag = np.vstack([mag[1:][::-1],mag])

plt.figure(1)
plt.contourf(X, Y, mag)
plt.colormaps()
plt.colorbar()

