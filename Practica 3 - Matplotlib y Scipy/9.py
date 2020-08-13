# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:51:55 2020

@author: santi
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import soundfile as sf

def codigo_tiempo(valor, posicion):
    out = ''
    if 0 < valor // 3600 < 10:
        out += '0'+str(int(valor // 3600))+':'
    elif valor // 3600 >= 10:
        out += str(int(valor // 3600))+':'
    valor = valor % 3600        
    if 60 > valor // 60 >= 10:
        out += str(int(valor // 60))+':'
    elif valor // 60 < 10:
        out += '0'+str(int(valor // 60))+':'
    if valor % 60 < 10:
        out += '0'+str(int(valor % 60))
    else:
        out += str(int(valor % 60))
        
    return out
        
def time_plot(audio):
    # audio, fs = sf.read()
    x = np.arange(len(audio)) / fs
    plt.figure(1)
    plt.plot(x, audio[:,0], label='L')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Audio')
    plt.grid()
    plt.gca().xaxis.set_major_formatter(FuncFormatter(codigo_tiempo))
    
x, fs = sf.read('audio73.wav')
time_plot(x)