# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:23:42 2020

@author: santi
"""


from tono import tono
import numpy as np
import notas_musicales as nm
import sounddevice as sd

def melodia(notas,valor,tempo):
    negra = 60/tempo
    melodia = np.empty(0)
    for i in range(len(notas)):
        nota = tono(valor[i]*negra*4, 44100, .5, notas[i])
        # sd.play(nota)
        melodia = np.hstack([melodia, nota])
    return melodia


notas_cucaracha = [nm.G4,nm.G4,nm.G4,nm.C5,nm.E5,nm.G4,nm.G4,nm.G4,nm.C5,
                   nm.E5,nm.C5,nm.C5,nm.B4,nm.B4,nm.A4,nm.A4,nm.G4]
valores_cucaracha = [1/8,1/8,1/8,3/8,2/8,1/8,1/8,1/8,3/8,6/8,2/8,1/8,1/8,1/8,1/8,1/8,8/8]

notas_marcha = [nm.Fs5,nm.D5,nm.B4,nm.Fs5,nm.D5,nm.B4,nm.Fs5,nm.D5,nm.Fs5,nm.D5,
                nm.B4,nm.Fs5,nm.D5,nm.B4,nm.E5,nm.Cs5]
valores_marcha = [1/4,1/8,1/8,1/4,1/8,1/8,1/2,1/2,1/4,1/8,1/8,1/4,1/8,1/8,1/2,1/2,]

nsim = [nm.F5,nm.Fs5,0,nm.G5,nm.G5,nm.Fs5,0,nm.F5,nm.Fs5,nm.G5,nm.Gs5,nm.G5,nm.G5,nm.Fs5]
vsim = [1/8,1/8,1/8,1/8,1/8,1/8,3/8,1/8,1/8,1/8,1/8,1/8,1/8,2/8]

nfc = [nm.C5,nm.C5,nm.D5,nm.C5,nm.F5,nm.E5,nm.C5,nm.C5,nm.D5,nm.C5,nm.G5,nm.F5]
vfc = [1/8,1/8,1/4,1/4,1/4,1/2]*2
# sd.play(melodia(notas_cucaracha,valores_cucaracha,152), 44100)
# sd.play(melodia(notas_marcha,valores_marcha,152), 44100)
# sd.play(melodia(nsim,vsim,112), 44100)
sd.play(melodia(nfc,vfc,112), 44100)


      