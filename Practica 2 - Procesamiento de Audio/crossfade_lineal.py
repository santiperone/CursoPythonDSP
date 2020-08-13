# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:21:48 2020

@author: santi
"""

import numpy as np

def crossfade_lineal(u,v,S):
    """
    realiza un crossfade lineal de n muestras entre los vectores u y v
    """
    crossu = u[len(u)-S:] * np.linspace(1,0,S)
    # print(crossu)
    crossv = v[0:S] * np.linspace(0,1,S)
    # print(crossv)
    crossfade = crossu + crossv
    return np.hstack([u[:len(u)-S],crossfade,v[S:]])