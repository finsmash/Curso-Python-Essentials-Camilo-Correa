# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:20:12 2023

@author: camil
"""

#uso de listas
#las listas es un conjunto de datos ordenado, python puede
# guardar una lista de valores 

lista=["1",2,3.5,True,"1"]
print(type(lista))

print(lista[0])

print(lista[1])

print(lista[3])

print(lista[4])

print(lista[-1])

print(lista[-5])

lista[4]="4"


del lista[4]
#uso de la tupla (conjunto ordenado de valores pero no son mutables)

tupla=("1",2,3.5,True,"1")
print(type(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla[4])
tupla[4]="4"
del tupla[4]
