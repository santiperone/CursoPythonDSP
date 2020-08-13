# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:08:54 2020

@author: santi
"""
import numpy as np
import sounddevice as sd

def tono(T, fs, A, f):
    muestra = 1 / fs
    tiempo = np.arange(0,T,muestra)
    a = 2 * np.pi * f * tiempo
    tono = A * np.sin(a)
    return tono

# sd.play(tono(3,44100,0.03,500))

def onda_triangular(T, fs, A, K, f):
    muestra = 1 / fs
    tiempo = np.arange(0,T,muestra)
    triangular = np.zeros(T * fs)
    for k in range(1,K+1):
        ck = (4 * (1-(-1)**k)) / np.square(np.pi * k)
        triangular += A * ck * np.cos(2 * np.pi * k * f * tiempo)
    return triangular

def min_distinto_cero(x):
    minimo = 1
    for i in range(0, len(x)):
        if x[i] < minimo and x[i] != 0:
            minimo = x[i]
    return minimo


def a_dbfs(x):
    x = abs(x)
    minimo = min_distinto_cero(x)
    for i in range(0, len(x)):
        if x[i] == 0:
            x[i] = minimo
    return 20 * np.log10(x)

def saw(T, fs, A, K, f):
    muestra = 1 / fs
    tiempo = np.arange(0,T,muestra)
    out = np.zeros(T * fs)
    for k in range(1,K+1):
        out += (np.sin(2 * np.pi * k * f * tiempo)) / k
    out *= (A * 4) / np.pi
    return out


def onda_cuadrada(T, fs, A, K, f):
    muestra = 1 / fs
    tiempo = np.arange(0,T,muestra)
    out = np.zeros(T * fs)
    for k in range(1,K+1,2):
        out += (np.sin(2 * np.pi * k * f * tiempo)) / k
    out *= (A * 4) / np.pi
    return out
