from enum import Enum


class Plaza:
    def __init__(self, tipo, precio, vacio, disponible):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.vacio = vacio
        self.disponible = disponible

    def __str__(self):
        return '{} {}'.format(self.id, self.tipo, self.tipo, self.precio, self.vacio, self.disponible)
