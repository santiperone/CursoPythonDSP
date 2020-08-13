# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:16:44 2020

@author: santi
"""
import numpy as np

def r_arange(n):
    """
    Crea rampa de n muestras con arange, dede 0 hasta 1
    """
    return np.arange(0,1 + 1/(n-1),1/(n-1))

def r_lins(n):
    return np.linspace(0,1,n)

def triangular(n):
    """
    devuelve onda triangular de 2n muestras
    """
    return np.hstack([r_arange(n),r_arange(n)[-2::-1]])