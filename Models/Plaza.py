from enum import Enum


class Plaza:
    def __init__(self, tipo, precio, ocupado, reservado, vehiculo):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.ocupado = ocupado
        self.reservado = reservado
        self.vehiculo = vehiculo

    def __str__(self):
        return '{} {}'.format(self.id, self.tipo, self.tipo, self.precio, self.ocupado, self.vehiculo)
