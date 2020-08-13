# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:06:41 2020

@author: santi
"""

def distorsion_valvular(x, y0):
    if x <= 0:
        return x
    else:
        return (y0 * x)/((1-y0)*x + y0)