# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# ### PROGRMAS RAMIFICADOS
# numero = int(input('Ingrese un numero entero: '))
# if (numero % 2 == 0):
#     print ('El numero es par')
# else:
#     print ('El numero es impar') 
# print('Fin')


# DIVISIBLE POR 2 y POR 3
numero = 9
# if numero % 2 == 0:
#     if numero % 3 == 0:
#         print('El numero',numero,'Es divisible por 2 y por 3')
#     else:
#         print('El numero',numero,'Es divisible por 2 pero no por 3')
# else 

# if (numero % 2 == 0) and (numero % 3 == 0):
#     print('El numero',numero,'Es divisible por 2 y por 3')
# elif (numero % 2 == 0) and (numero % 3 != 0):
#     print('El numero',numero,'Es divisible por 2 no por 3')
# elif (numero % 2 != 0) and (numero % 3 == 0):
#     print('El numero',numero,'No es divisible por 2 si por 3')

# SUMA DE 1 a 100
# hasta = 10000
# desde = 1
# suma = 0
# while (desde <= hasta):
#     suma = suma + desde
#     desde += 1
# print (suma)


# SUMA DE pares hasta 100
# hasta = 20
# desde = 1
# suma = 0
# while (desde % 2 != 0):
#     desde += 1
# while (desde <= hasta):
#     suma += desde
#     desde += 2
# print (suma)


### FOR LOOP
# SUMA LOS PRIMEROS 100 NATURALES
# resultado = 0
# for i in range(0,100):
#     reslultado += i

def perimetro(radio):
    return 2*3.1416*radio

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        