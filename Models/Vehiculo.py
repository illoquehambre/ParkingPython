from enum import Enum


class Vehiculo:
    def __init__(self, matricula, cliente):
        self.matricula = matricula
        self.cliente = cliente

    def __str__(self):
        return '{} {}'.format(self.matricula, self.cliente)
