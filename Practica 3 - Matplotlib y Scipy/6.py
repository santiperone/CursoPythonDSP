# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:28:11 2020

@author: santi
"""

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

ang = np.empty(0)
mag = np.empty(0)
for file in list(Path('./Directividad').glob('*.txt')):
    t = np.loadtxt(str(file), skiprows = 2, usecols = [0,1])
    ang = np.hstack([ang,(int((str(file)[25:-5])))])
    mag = np.hstack([mag,(t[list(t[:,0]).index(1000),1])])
ang = np.hstack([-ang[::-1],ang])
mag = np.hstack([mag[::-1],mag])

plt.figure(1)
plt.polar(ang * np.pi / 180, mag)
