# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:58:58 2020

@author: santi
"""

import tono as sw
import numpy as np
from matplotlib import pyplot as plt

tonoa = sw.tono(T=2, fs=44100, A=0.8,
f=1000)

tonob = sw.onda_triangular(T=2, fs=44100, A=0.8,
f=1000, K = 20)

tonoc = sw.saw(T=2, fs=44100, A=0.8,
f=1000, K = 20)

tonod = sw.onda_cuadrada(T=2, fs=44100, A=0.8,
f=1000, K = 9)

freqsa = np.fft.rfftfreq(len(tonoa), 1/44100)
fouriera = np.fft.rfft(tonoa)
espectroa = np.abs(fouriera)
espectroa[0] = 0
espectroa = espectroa / max(espectroa)

freqsb = np.fft.rfftfreq(len(tonob), 1/44100)
fourierb = np.fft.rfft(tonob)
espectrob = np.abs(fourierb)
espectrob[0] = 0
espectrob = espectrob / max(espectroa)

freqsc = np.fft.rfftfreq(len(tonoc), 1/44100)
fourierc = np.fft.rfft(tonoc)
espectroc = np.abs(fourierc)
espectroc[0] = 0
espectroc = espectroc / max(espectroc)

freqsd = np.fft.rfftfreq(len(tonod), 1/44100)
fourierd = np.fft.rfft(tonod)
espectrod = np.abs(fourierd)
espectrod[0] = 0
espectrod = espectrod / max(espectrod)


plt.figure(1)
plt.subplot(421)
plt.plot(freqsa, espectroa, 'r')
plt.grid()
plt.xlim([500, 20000])
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.subplot(422)
plt.plot(np.linspace(0,2,2*44100), tonoa, 'r')
plt.grid()
plt.xlim([0, .01])
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')

# plt.figure(2)
plt.subplot(423)
plt.plot(freqsb, espectrob, 'r')
plt.grid()
plt.xlim([500, 20000])
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.subplot(424)
plt.plot(np.linspace(0,2,2*44100), tonob, 'r')
plt.grid()
plt.xlim([0, .01])
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')

# plt.figure(3)
plt.subplot(425)
plt.plot(freqsc, espectroc, 'r')
plt.grid()
plt.xlim([500, 20000])
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.subplot(426)
plt.plot(np.linspace(0,2,2*44100), tonoc, 'r')
plt.grid()
plt.xlim([0, .01])
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')

# plt.figure(4)
plt.subplot(427)
plt.plot(freqsd, espectrod, 'r')
plt.grid()
plt.xlim([500, 20000])
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.subplot(428)
plt.plot(np.linspace(0,2,2*44100), tonod, 'r')
plt.grid()
plt.xlim([0, .01])
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')




