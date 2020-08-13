# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:51:55 2020

@author: santi
"""


import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf

def stereo_plot(audio):
    # audio, fs = sf.read()
    x = np.arange(len(audio)) / fs
    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, audio[:,0], label='L')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.title('Audio Stereo')
    plt.grid()
    
    plt.subplot(212)
    plt.plot(x/60, audio[:,1], label='R')
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Amplitud')
    plt.grid()
    
x, fs = sf.read('audio73.wav')
stereo_plot(x)