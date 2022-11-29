# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 06:40:02 2022

@author: Patricio Haro
"""

from random import randint
class Parqueadero():
    def __init__(self,marca, placa):
        self.marca = marca
        self.placa = placa
        self.color = "blanco"
        
    def asignar(self):
        parqueadero = []
        parqueadero.append(randint(0,20))
        par= parqueadero 
        return par
    
    def contar(a, b, c):
        marca = a 
        placa = b 
        auto1 = Parqueadero(placa, marca)
        auto1.color = c
        auto1.signar()
        print(auto1.marca)
        print(auto1.placa)
        print(auto1.asiganar)
        cont = 0
        if marca == "toyota":
            cont = cont +1
        return cont
    
 
     