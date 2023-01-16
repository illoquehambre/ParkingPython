from enum import Enum


class Vehiculo:
    def __init__(self, matricula, tipo, plaza):
        self.matricula = matricula
        self.tipo = tipo
        self.plaza = plaza

    def __str__(self):
        return '{} {}'.format(self.matricula, self.tipo, self.plaza)
