__author__ = 'jpino'



#!/usr/bin/env python

# -*- coding: utf-8 -*-



#Se importa el modulo unittest y math

import unittest
import math
#from django.test import TestCase
#from myapp.models import Animal

###### Archivo que contiene las clases y metodos para las pruebas unitarias con respecto a calculos matematicos ######

#Funcion raiz cuadrada.
def Raiz(a):
    #Si a es mayor o igual a cero se calcula la raiz cuadrada
    if a >= 0:
        return math.sqrt(a)
    #Si es menor a cero se genera una excepcion donde se informa que a debe ser mayor o igual a cero.
    else:
        raise ValueError,"a debe ser >= 0"



class RaizTest(unittest.TestCase):
    def test_Raiz(self):
        #Test para la raiz de nueve que devuelve 3 que debe pasar.
        self.assertEqual(3, Raiz(9))



    def test_zero(self):
        #Test para la raiz de 0 que devuelve 0, que debe pasar.
        self.assertEqual(0, Raiz(0))



### Comentar el metodo test_negative (y el self.assertRaises) para que pase la prueba
    def test_negative(self):
        #Test para la raiz de un numero negativo, que debe fallar.
        # Este debe devolver un ValueError, pero se espera un IndexError.
        self.assertRaises(IndexError, Raiz(-10))



if __name__ == '__main__':
    #Se ejecuta la prueba unitaria
    unittest.main()



