# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:53:45 2020

@author: santi
"""
import numpy as np

x = np.array([[1,2,1,0,-2],
              [0,0,-1,-1,8],
              [2,-1,6,2,7],
              [8,0,2,4,-4]])

a = x[1:3,2:4]
b = x[1:,1::2]