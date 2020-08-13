# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:28:11 2020

@author: santi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('mediciones.xlsx')

ang = np.empty(0)
for i in df.columns[1:]:
    ang = np.hstack([ang,int(i[7:])])
    
freq = df['frecuencia']
    
ang = np.hstack([-ang[1:][::-1],ang])
X, Y = np.meshgrid(freq,ang)
mag = df.loc[:, df.columns != 'frecuencia']
mag = np.transpose(mag)
mag = np.vstack([mag[1:][::-1],mag])

plt.figure(1)
plt.contourf(X, Y, mag)
plt.colormaps()
plt.colorbar()

    