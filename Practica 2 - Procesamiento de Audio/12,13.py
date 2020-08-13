# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:34:23 2020

@author: santi
"""
import numpy as np
from rms import rms

x = np.array([9, 8, 4, 6, -5, 5, -6, -2]) 

def envolvente_picos(x,w):
    picos = np.empty(0)
    for i in range(0,len(x),w):
        picos = np.hstack([picos,max(x[i:i+w])])
    return picos

def rms_por_ventanas(x,w):
    rmsv = np.empty(0)
    for i in range(0,len(x),w):
        rmsv = np.hstack([rmsv,rms(x[i:i+w])])
    return rmsv