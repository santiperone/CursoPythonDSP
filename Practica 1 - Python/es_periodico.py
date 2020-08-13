# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:34:18 2020

@author: santi
"""


# def es_periodica(x):    
#     for i in range(1,len(x)+1):
        
#         # print(i)
#         cont = 0
#         for p in x[-i-1::-1]:
#             # print(p)
#             cont += 1
#             if p == x[-i]:
#                 print(i)
#                 print(p)
#                 print(cont)
#                 print(x[-cont:-i])
                
                
def es_periodica(x):
    if x[:len(x)//2] == x[len(x)//2:]:
        return True
    
    for i in range(len(x)//2,len(x)-1):
        
        if x[i+1-len(x[i+1:]):i+1] == x[i+1:]:
            return True
    return False