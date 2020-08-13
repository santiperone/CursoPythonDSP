# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 01:06:02 2020

@author: santi
"""

import numpy as np

def rms(x):
    return np.sqrt(np.mean(x**2))

def rms_matriz(x):
    a = np.empty(0)
    print(a)
    for i in x:
        a = np.hstack([a,rms(i)])
    return a
