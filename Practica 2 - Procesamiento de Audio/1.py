# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:25:01 2020

@author: santi
"""
import numpy as np

a = np.arange(0,3)
b = np.arange(0,4)
c = np.arange(0,101)
d = np.arange(1,101)
e = np.arange(100,-1,-1)

f1 = np.arange(0,101) 
f2 = 9 * np.ones(101)
f = np.array([f1,f2])

g1 = f1
g2 = np.arange(30,231,2) / 10
g = np.array([g1,g2])

h1 = np.arange(3,8)
h2 = h1 ** 2
h3 = h1 ** 3
h = np.array([h1,h2,h3])

i1 = np.arange(0,201)
i2 = np.hstack([np.zeros(101),np.ones(100)])
i = np.vstack([i1,i2])