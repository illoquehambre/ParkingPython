from enum import Enum

from Models.Tipo import Tipo
from Models.Vehiculo import Vehiculo


class Plaza:
    def __init__(self, idPlaza, tipo, precio, ocupado, reservado, vehiculo=Vehiculo):
        self.id = id
        self.idPlaza = idPlaza
        self.tipo = tipo
        self.precio = precio
        self.ocupado = ocupado
        self.reservado = reservado
        self.vehiculo = vehiculo

    def __str__(self):
        return '{} {}'.format(self.id, self.idPlaza, self.tipo, self.tipo, self.precio, self.ocupado, self.vehiculo)
