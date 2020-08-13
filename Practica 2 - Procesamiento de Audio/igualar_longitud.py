# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:27:51 2020

@author: santi
"""

import numpy as np

def igualar_longitudes(x,y):
    relleno = np.zeros(abs(len(x)-len(y)))
    if len(x) > len(y):
        newy = np.hstack([y,relleno])
        return (x,newy)
    else:
        newx = np.hstack([x,relleno])
        return (newx,y)